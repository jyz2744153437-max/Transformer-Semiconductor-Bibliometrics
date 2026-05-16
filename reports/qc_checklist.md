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

- **注意项**：1 项（自引偏差，影响有限）
- **整体评级**：A 级（满足 L19-L20 全部核心要求）

---

## 七、【L21-L22 新增】写作质量自检

### 7.1 综述类型与方法透明

| # | 检查项 | 标准 | 状态 | 位置 |
|---|--------|------|------|------|
| 33 | 综述类型声明 | 明确为文献计量型 Review | ✅ | reports/review_type_statement.md |
| 34 | 方法 10 项透明清单 | 数据库/检索式/日期/时间/类型/纳入/排除/去重/工具/参数 | ✅ | reports/methods_draft.md §2.1 |
| 35 | 双数据集口径 | Methods 开头独立小节说明 643 与 147 各自用途 | ✅ | paper/manuscript_v1.md §2.1.1 |
| 36 | 各图表标注数据口径 | Results 各节标注基于全量还是 DL 纯净集 | ✅ | manuscript + results_paragraph_v1.md |

### 7.2 证据链与图表规范

| # | 检查项 | 标准 | 状态 | 位置 |
|---|--------|------|------|------|
| 37 | RQ-方法-图表映射 | 每个 RQ 对应明确的分析方法和图表 | ✅ | reports/method_result_map.csv |
| 38 | 证据链模型表 | Claim/Evidence/Lit/Interpretation/Boundary 五列 | ✅ | reports/claim_evidence_table.csv |
| 39 | 图注 7 要素 | 对象/数据源/时间/分析单位/工具版本/阈值/视觉元素 | ✅ | reports/results_paragraph_v1.md |
| 40 | 每图边界限制句 | "不能说明..." 或 "需注意..." | ✅ | results_paragraph_v1.md 每段结尾 |

### 7.3 写作规范

| # | 检查项 | 标准 | 状态 | 位置 |
|---|--------|------|------|------|
| 41 | IMRAD 结构完整 | Introduction-Methods-Results-Discussion-Conclusion | ✅ | paper/manuscript_v1.md |
| 42 | Introduction 四步骨架 | 背景→已有研究→缺口→本文目标+RQ | ✅ | reports/introduction_skeleton.md |
| 43 | Results 段落结构 | Claim→图号→指标→代表文献→解释→边界 | ✅ | reports/results_paragraph_v1.md |
| 44 | Discussion 趋势总结 | 基于证据指出方向，不含强立场预测 | ✅ | manuscript §4 |
| 45 | 不含过度推断 | 无"必将""一定""取代""已经成为主流" | ✅ | 全文搜索通过 |
| 46 | Conclusion 要素齐全 | 主要发现/贡献/局限性 | ✅ | manuscript §5 |

### 7.4 数据口径一致性

| # | 检查项 | 标准 | 状态 | 说明 |
|---|--------|------|------|------|
| 47 | 发文趋势数据口径 | 全量 643 + DL 纯净 147 双线 | ✅ | manuscript §3.1 |
| 48 | 国家/机构排名数据口径 | 全量 643 | ✅ | manuscript §3.2, §3.3 |
| 49 | CiteSpace 图谱数据口径 | DL 纯净 147 | ✅ | manuscript §3.4-3.7 |
| 50 | Python 网络分析数据口径 | DL 纯净 147 | ✅ | manuscript §3.8 |

---

## 自检结论（更新）

- **图谱/数据通过项**：25/26（96.2%）
- **写作质量通过项**：18/18（100%）
- **注意项**：1 项（自引偏差，影响有限）
- **整体评级**：A+ 级（满足 L1-L22 全部核心要求）
- **更新日期**：2026-05-16
