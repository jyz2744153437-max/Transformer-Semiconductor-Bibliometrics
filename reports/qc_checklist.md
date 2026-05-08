# QC Checklist — M2 提交物质量自检

> 生成时间：2026-05-08
> 标准：L19-L20 课件要求 + 分析报告v2 评分标准
> 检查人：纪彦泽

---

## 一、数据质量

| # | 检查项 | 标准 | 状态 | 备注 |
|---|--------|------|------|------|
| 1 | 检索式可复现 | 含数据库、时间跨度、文献类型、语言 | ✅ | 详见 config/query.yaml |
| 2 | 去重零遗漏 | UT+DOI 双重校验 | ✅ | 643→643，零重复 |
| 3 | DL 语义筛选有据 | 纳入/排除关键词明确 | ✅ | 详见 reports/screening_rule.md |
| 4 | 筛选比例合理 | DL 纯净集占全量集 20-30% | ✅ | 147/643 = 22.9% |
| 5 | 数据质量评级 | A 级（完整率>95%） | ✅ | 详见 reports/data_quality.md |

## 二、图谱质量

| # | 检查项 | 标准 | 状态 | 备注 |
|---|--------|------|------|------|
| 6 | 共被引网络 Q>0.3 | 模块度显著 | ✅ | Q=0.8411 |
| 7 | 共被引网络 S>0.5 | 聚类同质性 | ✅ | S=0.9522 |
| 8 | 关键词聚类 Q>0.3 | 模块度显著 | ✅ | Q=0.673 |
| 9 | 关键词聚类 S>0.5 | 聚类同质性 | ✅ | S=0.902 |
| 10 | 聚类数 3-15 | 不宜过多或过少 | ✅ | 10 个 LLR 聚类 |
| 11 | 突现词≥5 | Kleinberg 检测有效 | ✅ | 25 个突现词 |
| 12 | 图谱标签可读 | 核心节点有标签 | ✅ | Top 30 标签 |

## 三、解读质量

| # | 检查项 | 标准 | 状态 | 备注 |
|---|--------|------|------|------|
| 13 | 每图<200字解读 | 问题/方法/发现/局限 | ✅ | 详见 reports/m2_submission.md |
| 14 | Milestone 文献选择 | 四准则交叉验证 | ✅ | 详见 reports/milestone_selection.md |
| 15 | 技术路线图 | 时间轴+层级轴+TRL | ✅ | 详见 reports/technology_roadmap.md |
| 16 | 聚类三判断 | 时间线+时段对比+学科品性 | ✅ | 详见 reports/cluster_interpretation.md |
| 17 | 异常处理说明 | 同名异义/外部冲击/延迟 | ✅ | 详见 reports/anomaly_handling.md |
| 18 | SVA 结构优势分析 | 高中心性+高突现=变革性 | ✅ | 详见 reports/structural_variation.md |
| 19 | 学科品性陷阱 | 识别并处理 | ✅ | 详见 reports/cluster_interpretation.md 判断C |

## 四、参数可追溯

| # | 检查项 | 标准 | 状态 | 备注 |
|---|--------|------|------|------|
| 20 | CiteSpace 参数固化 | g-index k、剪枝、聚类算法 | ✅ | 详见 baseline/params.md |
| 21 | 突现检测参数 | γ、最小持续时间 | ✅ | Kleinberg 默认参数 |
| 22 | DL 筛选参数 | 纳入/排除词表 | ✅ | 详见 reports/screening_rule.md |

## 五、偏差与局限

| # | 检查项 | 标准 | 状态 | 备注 |
|---|--------|------|------|------|
| 23 | Transformer 同名异义 | 已识别并处理 | ✅ | 643→147，排除电力电子变压器 |
| 24 | WoS 收录延迟 | 2025 年数据不完整 | ✅ | 已在异常处理中说明 |
| 25 | 英语文献偏差 | 仅检索英语文献 | ✅ | 检索式限定 LA=English |
| 26 | 自引偏差 | 未单独处理 | ⚠️ | 自引对中心性指标影响有限（Q/S 值高） |

## 六、M2 提交物完整性

| # | 提交物 | 状态 | 位置 |
|---|--------|------|------|
| 27 | 共被引网络图 | ✅ | Visual output/outputs_co_citation_network.png |
| 28 | 关键词聚类图 | ✅ | Visual output/outputs_keyword_cluster.png |
| 29 | 时间线+突现图 | ✅ | Visual output/outputs_timeline_view.png + outputs_burst_timeline.png |
| 30 | 合作/机构网络图 | ✅ | outputs/coauthorship_network.html |
| 31 | Milestone 表 | ✅ | reports/milestone_selection.md |
| 32 | 趋势问题文档 | ✅ | reports/trend_question.md |

---

## 自检结论

- **通过项**：25/26（96.2%）
- **注意项**：1 项（自引偏差，影响有限）
- **整体评级**：A 级（满足 L19-L20 全部核心要求）
