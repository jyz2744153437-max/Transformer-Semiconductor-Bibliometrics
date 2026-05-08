"""按交接要求生成四个交互式网络图 HTML。"""
from pathlib import Path
import sys
import re

import networkx as nx
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# 尝试导入 WoS 解析器以建立 UT→标题映射
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

TOP_LABELS = 30
EDGE_LIMIT = 150
MIN_SIZE = 10
MAX_SIZE = 55
LAYOUT_K = 3.5
LAYOUT_ITERATIONS = 150


def clean_text(value):
    text = '' if pd.isna(value) else str(value)
    return ' '.join(text.replace('_', ' ').split())


def shorten_text(text, limit):
    text = clean_text(text)
    if len(text) <= limit:
        return text
    return text[: limit - 3] + '...'


def beautify_node_name(raw, network_key):
    """将原始节点名转为可读的短名（用于标签显示）。"""
    if network_key == 'co_citation':
        # "Dosovitskiy A_2021_Arxiv" → "Dosovitskiy A (2021)"
        m = re.match(r'^(.+?)_(\d{4})_', raw)
        if m:
            return f'{m.group(1)} ({m.group(2)})'
        m = re.match(r'^(.+?)_(\d{4})$', raw)
        if m:
            return f'{m.group(1)} ({m.group(2)})'
        return raw

    if network_key == 'bibliographic_coupling':
        # WOS:000123456789 → "Author (Year) Title..."
        if raw in UT_MAP:
            info = UT_MAP[raw]
            author = info['author']
            year = info['year']
            return f'{author} ({year})' if year else author
        return raw

    return raw


def full_node_info(raw, network_key):
    """返回悬停用的完整节点信息。"""
    if network_key == 'bibliographic_coupling' and raw in UT_MAP:
        info = UT_MAP[raw]
        parts = []
        if info['author']:
            parts.append(info['author'])
        if info['year']:
            parts.append(f'({info["year"]})')
        if info['title']:
            parts.append(info['title'][:80])
        return ' '.join(parts) if parts else raw

    if network_key == 'co_citation':
        # 展示完整引用信息
        return raw.replace('_', ' ')

    return raw


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
        if not source or not target:
            continue
        if source == target:
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


def build_community_map(graph, metric_lookup):
    community_map = {}
    for node in graph.nodes():
        metrics = metric_lookup.get(node)
        if metrics is not None:
            community_map[node] = metrics['community']

    if community_map:
        return community_map

    communities = nx.algorithms.community.greedy_modularity_communities(graph, weight='weight')
    for community_id, nodes in enumerate(communities):
        for node in nodes:
            community_map[node] = community_id
    return community_map


def build_layout(graph):
    node_count = max(graph.number_of_nodes(), 1)
    return nx.spring_layout(
        graph,
        seed=42,
        weight='weight',
        k=LAYOUT_K / np.sqrt(node_count),
        iterations=LAYOUT_ITERATIONS,
    )


def build_edge_traces(graph, positions):
    strongest_edges = sorted(
        graph.edges(data=True),
        key=lambda item: item[2].get('weight', 1),
        reverse=True,
    )[:EDGE_LIMIT]

    if not strongest_edges:
        return []

    max_weight = max(edge[2].get('weight', 1) for edge in strongest_edges)
    traces = []
    for source, target, data in strongest_edges:
        weight = data.get('weight', 1)
        x0, y0 = positions[source]
        x1, y1 = positions[target]
        traces.append(
            go.Scatter(
                x=[x0, x1, None],
                y=[y0, y1, None],
                mode='lines',
                line=dict(
                    width=0.4 + 2.6 * (weight / max_weight),
                    color='rgba(140, 152, 164, 0.35)',
                ),
                hoverinfo='text',
                text=(
                    f'{shorten_text(source, 45)} ↔ {shorten_text(target, 45)}'
                    f'<br>权重: {weight:.1f}'
                ),
                hoverlabel=dict(bgcolor='white', font_size=10),
                showlegend=False,
            )
        )
    return traces


def build_node_trace(graph, positions, metric_lookup, community_map, node_label, network_key):
    weighted_degree_map = dict(graph.degree(weight='weight'))
    max_weighted_degree = max(weighted_degree_map.values(), default=1)

    node_x = []
    node_y = []
    node_sizes = []
    node_colors = []
    node_hover = []

    for node in graph.nodes():
        x, y = positions[node]
        node_x.append(x)
        node_y.append(y)

        metrics = metric_lookup.get(node, {})
        weighted_degree = float(metrics.get('weighted_degree', weighted_degree_map.get(node, 0)))
        degree = int(metrics.get('degree', graph.degree(node)))
        betweenness = float(metrics.get('betweenness', 0))
        pagerank = float(metrics.get('pagerank', 0))
        community = community_map.get(node, 0)

        node_sizes.append(MIN_SIZE + (MAX_SIZE - MIN_SIZE) * (weighted_degree / max(max_weighted_degree, 1)))
        node_colors.append(CLUSTER_COLORS[community % len(CLUSTER_COLORS)])

        display_name = beautify_node_name(node, network_key)
        hover_info = full_node_info(node, network_key)
        node_hover.append(
            '<br>'.join([
                f'<b>{shorten_text(hover_info, 80)}</b>',
                f'{node_label}: {shorten_text(display_name, 70)}',
                f'社团: {community}',
                f'度: {degree}',
                f'加权度: {weighted_degree:.1f}',
                f'中介中心性: {betweenness:.4f}',
                f'PageRank: {pagerank:.4f}',
            ])
        )

    weighted_degree_rank = sorted(
        graph.nodes(),
        key=lambda node: float(metric_lookup.get(node, {}).get('weighted_degree', weighted_degree_map.get(node, 0))),
        reverse=True,
    )

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode='markers',
        marker=dict(
            color=node_colors,
            size=node_sizes,
            line=dict(width=1.2, color='#2c3e50'),
            opacity=0.92,
        ),
        text=node_hover,
        hoverinfo='text',
        hoverlabel=dict(bgcolor='white', font_size=11, align='left'),
        showlegend=False,
    )

    label_nodes = [node for node in weighted_degree_rank[:TOP_LABELS] if node in positions]
    label_trace = go.Scatter(
        x=[positions[node][0] for node in label_nodes],
        y=[positions[node][1] for node in label_nodes],
        mode='text',
        text=[shorten_text(beautify_node_name(node, network_key), 22) for node in label_nodes],
        textposition='top center',
        textfont=dict(size=9, color='#1f2933'),
        hoverinfo='none',
        showlegend=False,
    )

    return node_trace, label_trace


def add_community_legend(fig, community_map):
    for community in sorted(set(community_map.values())):
        count = sum(1 for value in community_map.values() if value == community)
        fig.add_trace(
            go.Scatter(
                x=[None],
                y=[None],
                mode='markers',
                marker=dict(
                    size=11,
                    color=CLUSTER_COLORS[community % len(CLUSTER_COLORS)],
                    line=dict(width=1, color='#2c3e50'),
                ),
                name=f'社团 {community}（{count} 节点）',
                showlegend=True,
            )
        )


def write_network_html(network_key, config):
    graph, metrics = load_graph(config['edge_file'], config['metric_file'])
    if graph.number_of_nodes() == 0:
        raise ValueError(f'{network_key} 图为空，无法生成 HTML')

    metric_lookup = build_metric_lookup(metrics)
    community_map = build_community_map(graph, metric_lookup)
    positions = build_layout(graph)

    edge_traces = build_edge_traces(graph, positions)
    node_trace, label_trace = build_node_trace(
        graph,
        positions,
        metric_lookup,
        community_map,
        config['label'],
        network_key,
    )

    figure = go.Figure(data=edge_traces + [node_trace, label_trace])
    add_community_legend(figure, community_map)
    figure.update_layout(
        title=dict(text=f'<b>{config["title"]}</b>', font_size=18),
        hovermode='closest',
        showlegend=True,
        legend=dict(
            x=1.02,
            y=1.0,
            bgcolor='rgba(255,255,255,0.92)',
            bordercolor='#d9e2ec',
            borderwidth=1,
            font=dict(size=10),
        ),
        margin=dict(l=20, r=190, b=20, t=60),
        paper_bgcolor='white',
        plot_bgcolor='white',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    )

    output_path = Path(f'outputs/{network_key}_network.html')
    figure.write_html(
        str(output_path),
        include_plotlyjs='cdn',
        config={
            'scrollZoom': True,
            'displayModeBar': True,
            'modeBarButtonsToRemove': ['lasso2d'],
        },
    )

    print(
        f'OK {output_path} | nodes={graph.number_of_nodes()} '
        f'edges={graph.number_of_edges()} shown_edges={min(graph.number_of_edges(), EDGE_LIMIT)} '
        f'labels={TOP_LABELS}'
    )


def main():
    selected = sys.argv[1:] if len(sys.argv) > 1 else list(NETWORK_CONFIGS.keys())
    for network_key in selected:
        if network_key not in NETWORK_CONFIGS:
            print(f'Skipping unknown network: {network_key}')
            continue
        print(f'Generating {NETWORK_CONFIGS[network_key]["title"]}...')
        write_network_html(network_key, NETWORK_CONFIGS[network_key])


if __name__ == '__main__':
    main()
