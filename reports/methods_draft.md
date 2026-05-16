# 方法部分初稿（含 10 项透明清单 + 双数据集口径）

> 生成时间：2026-05-16
> 依据：L21 课件（Data and Methods 透明报告要求）+ L22 课件（图注 7 要素）
> 对应 manuscript Section 2 的完整版

---

## 2.1 数据来源（10 项透明清单）

| # | 项目 | 本文取值 |
|---|------|----------|
| 1 | 数据库 | Web of Science Core Collection |
| 2 | 检索式 | TS=(Transformer 及其 6 种变体) AND TS=(半导体制造 6 个场景词) NOT TS=(11 类排除词) |
| 3 | 检索日期 | 2026-04-14 |
| 4 | 时间范围 | 2015-2025 |
| 5 | 文献类型 | Article / Review / Proceedings Paper |
| 6 | 纳入标准 | 标题/摘要含 attention mechanism, vision transformer, deep learning, ViT, Swin, self-attention 等 DL 信号词 |
| 7 | 排除标准 | 标题/摘要含 power amplifier, MMIC, DC-DC converter, Doherty, RFID tag, inductive coupling, flyback converter 等电力/射频信号词 |
| 8 | 去重与清洗规则 | UT + DOI 双重校验去重；同义词映射（ViT→Vision Transformer 等） |
| 9 | 分析工具和版本 | CiteSpace 6.4.1 (Standard 版)；Python bibliometrics-mini (networkx + pandas + plotly) |
| 10 | 关键参数和阈值 | 时间切片 Slice=1；g-index k=25；Pathfinder + Pruning sliced networks；LLR 聚类标签；Cosine 相似度 |

## 2.2 双数据集口径对照

| 数据集 | 文献量 | 构成 | 分析用途 |
|--------|--------|------|----------|
| 全量集 | 643 篇 | WoS 原文原貌导出，含 77% 非 DL 文献 | 国家/地区分布、机构分布、发文趋势总量基准 |
| DL 纯净集 | 147 篇 | 标题/摘要语义筛选后的 DL Transformer 文献 | CiteSpace 全部图谱 + Python 网络分析 + 结论解读 |

## 2.3 检索式（v2-final）

```
TS=("Transformer" OR "Vision Transformer" OR "ViT" OR "Swin Transformer"
   OR "Autoformer" OR "Informer" OR "PatchTST")
AND TS=("semiconductor" OR "wafer" OR "integrated circuit" OR "lithography"
   OR "semiconductor packaging" OR "wafer fabrication" OR "chip manufacturing")
NOT TS=("power transformer" OR "voltage" OR "current transformer"
   OR "medical image" OR "NLP" OR "natural language"
   OR "traffic" OR "power load" OR "smart grid"
   OR "distribution network" OR "financial")
```

检索式迭代：v0 (105条) → v1 (512条) → v2-final (643条)，详见 `config/query.yaml`。

## 2.4 筛选流程（PRISMA 2020）

```
Identification  → WoS 检索 n=643
Screening       → 去重 (UT+DOI 双重校验) n=643 (零重复)
                → DL 语义筛选 n=147 (排除 496 篇电力/射频文献)
Eligibility     → 字段完整性复核 n=147 (无缺失)
Included        → 最终纳入 n=147 (DL 纯净集)
```

详见 `reports/prisma_flowchart.md`。

## 2.5 分析方法

| 分析类型 | 方法 | 工具 | 输入数据 |
|----------|------|------|----------|
| 发文趋势 | 年度发文量统计 + 增长率 | Python/pandas | 全量 643 + DL 纯净 147 |
| 关键词共现聚类 | 共现矩阵 → Louvain 聚类 → LLR 标签 | CiteSpace 6.4.1 | DL 纯净 147 |
| 共被引网络 | C=AᵀA → g-index k=25 → 聚类 | CiteSpace 6.4.1 | DL 纯净 147 |
| 突现检测 | Kleinberg 算法 (s=2, γ=1) | CiteSpace 6.4.1 | DL 纯净 147 |
| 合作网络 | MᵀM → 贪婪模块度社团检测 | Python/networkx | DL 纯净 147 |
| 网络指标 | Degree/Betweenness/PageRank 等 8 项 | Python/networkx | DL 纯净 147 |
| Milestone 识别 | 四准则交叉验证（被引+突现+中心性+Sigma） | Python + CiteSpace | DL 纯净 147 |

## 2.6 网络定义四要素

| 要素 | 共被引网络 | 关键词共现网络 | 合作网络 |
|------|-----------|---------------|---------|
| 节点 | 被引文献 | 关键词 | 作者 |
| 边 | 两篇文献被同一施引文献引用 | 两词出现在同一篇文章 | 两作者共同发表 |
| 权重 | 共被引频次 | 共现频次 | 合著论文数 |
| 阈值 | g-index k=25 | g-index k=25 | 无阈值 |

---

## 自检

- [x] 10 项透明清单全部覆盖
- [x] 双数据集口径对照表
- [x] PRISMA 筛选流程
- [x] 网络定义四要素
- [x] 参数可追溯
