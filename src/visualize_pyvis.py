"""用 Pyvis 生成四个交互式网络图 HTML（力导向、可拖拽、点击弹详情）。"""
from pathlib import Path
import sys
import re

import networkx as nx
import pandas as pd
from pyvis.network import Network

# 导入 WoS 解析器以建立 UT→标题映射
try:
    sys.path.insert(0, '课件及杂项/课件及老师发的文件/bibliometrics-mini-template/bibliometrics-mini-template/src')
    from bmmini.parse_wos import parse_wos_dir
    _WOS_RECORDS = parse_wos_dir('Data')
    UT_MAP = {}
    for _r in _WOS_RECORDS:
        _ut = _r.get('UT', '').strip()
        _ti = _r.get('TI', '').strip()
        _au = _r.get('AU', '').strip().split(';')[0].strip() if _r.get('AU', '') else ''
        _py = _r.get('PY', '').strip()
        if _ut:
            UT_MAP[_ut] = {'title': _ti, 'author': _au, 'year': _py}
except Exception:
    UT_MAP = {}

CLUSTER_COLORS = [
    '#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6',
    '#1abc9c', '#e67e22', '#34495e', '#16a085', '#c0392b',
    '#2980b9', '#27ae60', '#d35400', '#8e44ad', '#f1c40f',
    '#7f8c8d', '#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4',
]

NETWORK_CONFIGS = {
    'keyword_cooccurrence': {
        'title': '关键词共现网络',
        'edge_file': 'outputs/keyword_cooccurrence_edges.csv',
        'metric_file': 'outputs/network_metrics_keyword_cooccurrence.csv',
        'label': '关键词',
    },
    'co_citation': {
        'title': '共被引网络',
        'edge_file': 'outputs/co_citation_edges.csv',
        'metric_file': 'outputs/network_metrics_co_citation.csv',
        'label': '被引文献',
    },
    'bibliographic_coupling': {
        'title': '文献耦合网络',
        'edge_file': 'outputs/bibliographic_coupling_edges.csv',
        'metric_file': 'outputs/network_metrics_bibliographic_coupling.csv',
        'label': '施引文献',
    },
    'coauthorship': {
        'title': '合作网络',
        'edge_file': 'outputs/coauthorship_edges.csv',
        'metric_file': 'outputs/network_metrics_coauthorship.csv',
        'label': '作者',
    },
}


def clean_text(value):
    text = '' if pd.isna(value) else str(value)
    return ' '.join(text.replace('_', ' ').split())


def beautify_node_name(raw, network_key):
    if network_key == 'co_citation':
        m = re.match(r'^(.+?)_(\d{4})_', raw)
        if m:
            return f'{m.group(1)} ({m.group(2)})'
        m = re.match(r'^(.+?)_(\d{4})$', raw)
        if m:
            return f'{m.group(1)} ({m.group(2)})'
        return raw
    if network_key == 'bibliographic_coupling':
        if raw in UT_MAP:
            info = UT_MAP[raw]
            author = info['author']
            year = info['year']
            return f'{author} ({year})' if year else author
        return raw
    return raw


def build_tooltip(node, metrics, network_key):
    """构建 Pyvis 节点悬停提示（仅用 <br>/<b>，复杂 CSS 在 vis.js 中不渲染）。"""
    degree = metrics.get('degree', 0)
    wd = metrics.get('weighted_degree', 0)
    bet = metrics.get('betweenness', 0)
    pr = metrics.get('pagerank', 0)
    comm = metrics.get('community', 0)
    return (
        f'社团: <b>{comm}</b><br>'
        f'度: <b>{degree}</b>'
        f'  |  加权度: <b>{wd:.1f}</b><br>'
        f'中介中心性: <b>{bet:.4f}</b>'
        f'  |  PageRank: <b>{pr:.4f}</b>'
    )


def load_graph(edge_file, metric_file):
    edges = pd.read_csv(edge_file)
    metrics = pd.read_csv(metric_file)
    graph = nx.Graph()
    metric_nodes = set()
    for _, row in metrics.iterrows():
        node = clean_text(row['node'])
        metric_nodes.add(node)
        graph.add_node(node)
    for _, row in edges.iterrows():
        source = clean_text(row['source'])
        target = clean_text(row['target'])
        if not source or not target or source == target:
            continue
        weight = float(row['weight'])
        graph.add_edge(source, target, weight=weight)
        if source not in metric_nodes:
            graph.add_node(source)
        if target not in metric_nodes:
            graph.add_node(target)
    return graph, metrics


def build_metric_lookup(metrics):
    lookup = {}
    for _, row in metrics.iterrows():
        node = clean_text(row['node'])
        lookup[node] = {
            'degree': int(row['degree']),
            'weighted_degree': float(row['weighted_degree']),
            'betweenness': float(row['betweenness']),
            'pagerank': float(row['pagerank']),
            'closeness': float(row['closeness']),
            'eigenvector': float(row['eigenvector']),
            'community': int(row['community']),
        }
    return lookup


def write_pyvis_html(network_key, config):
    graph, metrics = load_graph(config['edge_file'], config['metric_file'])
    if graph.number_of_nodes() == 0:
        raise ValueError(f'{network_key} 图为空')

    metric_lookup = build_metric_lookup(metrics)
    weighted_degree_map = dict(graph.degree(weight='weight'))
    max_wd = max(weighted_degree_map.values(), default=1)

    # 社团映射
    community_map = {}
    for node in graph.nodes():
        m = metric_lookup.get(node)
        if m is not None:
            community_map[node] = m['community']
    if not community_map:
        communities = nx.algorithms.community.greedy_modularity_communities(graph, weight='weight')
        for cid, nodes in enumerate(communities):
            for node in nodes:
                community_map[node] = cid

    # 创建 Pyvis 网络
    net = Network(
        height='750px',
        width='100%',
        bgcolor='white',
        font_color='#2c3e50',
        directed=False,
        notebook=False,
    )
    # 不设 heading——Pyvis 对中文有编码 bug，保存后手动修复

    # 添加节点
    for node in graph.nodes():
        m = metric_lookup.get(node, {})
        wd = float(m.get('weighted_degree', weighted_degree_map.get(node, 0)))
        comm = community_map.get(node, 0)
        color = CLUSTER_COLORS[comm % len(CLUSTER_COLORS)]
        size = 10 + 40 * (wd / max(max_wd, 1))
        label = beautify_node_name(node, network_key)
        title = build_tooltip(node, m, network_key)
        net.add_node(
            node,
            label=label,
            title=title,
            size=size,
            color=color,
            borderWidth=1,
            borderWidthSelected=2,
        )

    # 添加边（只取最强 150 条）
    strongest = sorted(
        graph.edges(data=True),
        key=lambda item: item[2].get('weight', 1),
        reverse=True,
    )[:150]
    max_edge_w = max((d.get('weight', 1) for _, _, d in strongest), default=1)
    for source, target, data in strongest:
        w = data.get('weight', 1)
        width = 0.5 + 4.5 * (w / max_edge_w)
        net.add_edge(
            source, target,
            value=w,
            width=width,
            color='rgba(140,152,164,0.4)',
            title=f'{beautify_node_name(source, network_key)} ↔ {beautify_node_name(target, network_key)}<br>权重: {w:.1f}',
        )

    # 物理模拟参数
    net.set_options("""
    {
        "physics": {
            "barnesHut": {
                "gravitationalConstant": -8000,
                "centralGravity": 0.3,
                "springLength": 150,
                "springConstant": 0.04,
                "damping": 0.09
            },
            "stabilization": {
                "iterations": 200
            }
        },
        "interaction": {
            "hover": true,
            "tooltipDelay": 100,
            "navigationButtons": true,
            "keyboard": true
        }
    }
    """)

    output_path = Path(f'outputs/{network_key}_network_pyvis.html')
    net.save_graph(str(output_path))

    # Pyvis 对中文 heading 有编码 bug，保存后手动修复标题
    html = output_path.read_text(encoding='utf-8', errors='replace')
    correct_title = f'<h3 style="text-align:center">{config["title"]}</h3>'
    # Pyvis 生成 <center><h1></h1></center>（空标题），替换为正确中文
    html = re.sub(
        r'<center>\s*<h1>.*?</h1>\s*</center>',
        f'<center><h1>{correct_title}</h1></center>',
        html,
    )
    output_path.write_text(html, encoding='utf-8')

    print(
        f'OK {output_path} | nodes={graph.number_of_nodes()} '
        f'edges={graph.number_of_edges()} shown_edges={min(graph.number_of_edges(), 150)}'
    )


def main():
    selected = sys.argv[1:] if len(sys.argv) > 1 else list(NETWORK_CONFIGS.keys())
    for network_key in selected:
        if network_key not in NETWORK_CONFIGS:
            print(f'Skipping unknown network: {network_key}')
            continue
        print(f'Generating {NETWORK_CONFIGS[network_key]["title"]} (Pyvis)...')
        write_pyvis_html(network_key, NETWORK_CONFIGS[network_key])


if __name__ == '__main__':
    main()
