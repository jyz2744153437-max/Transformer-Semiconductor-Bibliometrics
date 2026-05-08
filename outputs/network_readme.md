# 交互式网络图说明

> 生成时间：2026-05-08
> 每种网络提供两个版本：Plotly 版（课程模板标准）和 Pyvis 版（增强交互体验）

---

## 两种版本对比

| 特性 | Plotly 版（`*_network.html`） | Pyvis 版（`*_network_pyvis.html`） |
|------|------|------|
| **技术** | Python + Plotly（课程模板标准） | Python + Pyvis（基于 vis.js） |
| **节点拖拽** | ❌ 不支持 | ✅ 可拖拽，物理模拟自动回弹 |
| **整体缩放** | ✅ 滚轮缩放 | ✅ 滚轮缩放 |
| **整体平移** | ✅ 拖拽画布 | ✅ 拖拽画布 |
| **悬停信息** | ✅ 显示指标卡片 | ✅ 显示指标卡片 |
| **图例筛选** | ✅ 点击图例筛选社团 | ❌ 无图例筛选 |
| **节点点击** | 无额外效果 | ✅ 高亮连接的邻居节点 |
| **物理模拟** | ❌ 静态布局 | ✅ 力导向自动布局 |
| **搜索定位** | ❌ 无 | ✅ 浏览器 Ctrl+F 搜索节点名 |
| **导航按钮** | ❌ 无 | ✅ 缩放、全屏、重置按钮 |
| **课程要求** | ✅ 满足模板标准 | 补充增强，非必需 |

---

## 四种网络

| 网络 | Plotly 版 | Pyvis 版 | 解读方向 |
|------|-----------|----------|----------|
| 关键词共现 | [keyword_cooccurrence_network.html](keyword_cooccurrence_network.html) | [keyword_cooccurrence_network_pyvis.html](keyword_cooccurrence_network_pyvis.html) | 识别研究热点，同色=同主题聚类 |
| 共被引 | [co_citation_network.html](co_citation_network.html) | [co_citation_network_pyvis.html](co_citation_network_pyvis.html) | 揭示知识基础，球大=奠基文献 |
| 文献耦合 | [bibliographic_coupling_network.html](bibliographic_coupling_network.html) | [bibliographic_coupling_network_pyvis.html](bibliographic_coupling_network_pyvis.html) | 发现研究前沿 |
| 合作网络 | [coauthorship_network.html](coauthorship_network.html) | [coauthorship_network_pyvis.html](coauthorship_network_pyvis.html) | 识别核心团队与机构 |

---

## 操作指南

### Plotly 版
- **缩放**：滚轮
- **平移**：拖拽画布空白处
- **悬停**：鼠标移到节点上弹出指标卡片
- **筛选**：点击右侧图例隐藏/显示某个社团

### Pyvis 版
- **缩放**：滚轮或右下角按钮
- **平移**：拖拽画布空白处
- **拖拽节点**：按住节点拖动，松开后物理模拟自动调整
- **悬停**：鼠标移到节点上弹出指标卡片
- **点击节点**：高亮该节点的所有邻居
- **搜索**：浏览器 Ctrl+F 搜索节点名
- **导航**：右下角按钮可缩放、全屏、重置视图

---

## 节点大小与颜色

- **大小**：按加权度（weighted degree），球越大=连接越密集
- **颜色**：按社团（community），同色=同主题/同团队
- **边粗细**：按权重，越粗=关联越强

---

## 生成脚本

| 版本 | 脚本 | 运行命令 |
|------|------|----------|
| Plotly | `src/visualize_interactive.py` | `python src/visualize_interactive.py` |
| Pyvis | `src/visualize_pyvis.py` | `python src/visualize_pyvis.py` |
