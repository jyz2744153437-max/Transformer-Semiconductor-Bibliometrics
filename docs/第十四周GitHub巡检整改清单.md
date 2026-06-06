# 第十四周 GitHub 巡检整改清单（Lesson 27-28）

> 更新日期：2026-06-06
> 依据：`文献计量学课件 Lesson27 & 28(1).pdf`
> 用途：按第 27、28 次课的“2 分钟 GitHub 闪检”口径，集中说明本项目材料在哪里、能否复现、下一步还缺什么。

---

## 1. 课堂要求摘要

第 14 周不是预答辩，而是期末规则说明与 GitHub 项目巡检。老师主要检查三件事：

1. 材料在哪里：README、论文、数据、参数、图表、AI 使用说明、分工记录。
2. 能否复现：依赖文件、运行命令、输入数据、稳定输出目录。
3. 下一步修什么：记录 Top1 整改项、负责人、完成状态。

---

## 2. 六类最终成果包对照

| 课件要求 | 本项目对应位置 | 当前状态 | 说明 |
|---|---|---|---|
| 课程论文 mini review | `paper/manuscript_v1.md` | 已完成主稿 | 采用 IMRaD 框架，围绕 RQ、Methods、Results、Discussion、Conclusion 组织 |
| GitHub 仓库与运行说明 | `README.md`、`run_pipeline.py`、`requirements.txt` | 已具备 | README 含项目简介、数据来源、方法、输出目录与快速复现命令 |
| 数据与图表 | `Data/`、`Visual output/`、`outputs/`、`baseline/params.md` | 已具备 | 原始数据、DL 纯净集、CiteSpace 图谱、交互网络与参数文件均可定位 |
| AI 使用说明 | `docs/引用库与AI伦理说明.md`、`docs/智能体工作流总览.md` | 已具备 | 说明 AI 参与边界、用途和人工复核方式 |
| 答辩材料 | `项目展示.html`、`presentation/README.md` | 已具备 | HTML 为主讲材料，PPT/PDF 备份策略见 presentation 索引 |
| 个人材料 | `docs/团队分工.md`、`reflection/README.md` | 已具备索引 | 分工记录已落在 docs，个人反思可按 reflection 模板补充 |

---

## 3. Methods 透明度 10 项自检

| # | 课件要求 | 本项目对应内容 | 位置 |
|---|---|---|---|
| 1 | 数据库名称 | Web of Science Core Collection | `README.md`、`Data/README.md`、`reports/methods_draft.md` |
| 2 | 完整检索式 | v2-final 检索式与迭代历史 | `config/query.yaml`、`docs/query_rationale.md`、`docs/query_changelog.md` |
| 3 | 检索日期 | 2026-04-14 | `README.md`、`Data/README.md`、`reports/methods_draft.md` |
| 4 | 时间范围 | 2015-2025 | `README.md`、`paper/manuscript_v1.md` |
| 5 | 文献类型 | Article / Review / Proceedings Paper | `README.md`、`Data/README.md` |
| 6 | 纳入标准 | DL Transformer 语义筛选信号词 | `reports/screening_rule.md`、`reports/methods_draft.md` |
| 7 | 排除标准 | 电力电子/射频等非 DL transformer 语义排除 | `reports/screening_rule.md`、`docs/分析口径对照表.md` |
| 8 | 去重与清洗规则 | UT + DOI 双重校验；语义筛选为 147 篇 DL 纯净集 | `reports/screening_record.md`、`Data/README.md` |
| 9 | 分析工具和版本 | CiteSpace 6.4.1；Python networkx/pandas/plotly 辅助复核 | `baseline/tool_selection.md`、`reports/methods_draft.md` |
| 10 | 关键参数和阈值 | g-index k=25；Pathfinder；Pruning sliced networks；LLR | `baseline/params.md`、`CiteSpace分析套件/3_CiteSpace参数设置.md` |

结论：10 项透明度要求均已有明确落点，答辩时优先打开 `reports/methods_draft.md` 和 `baseline/params.md`。

---

## 4. 3 图 1 表与 RQ 对照

| 课件最低要求 | 本项目材料 | 回答的 RQ/子问题 |
|---|---|---|
| Fig.1 年发文趋势 | `outputs/发文趋势图.html`、`outputs/发文趋势_年度统计.csv` | Transformer 半导体研究何时进入加速期？ |
| Fig.2 合作网络 | `outputs/coauthorship_network.html`、`outputs/coauthorship_network_pyvis.html`、相关 metrics CSV | 研究力量如何分布，合作结构是否集中？ |
| Fig.3 关键词/共被引/主题演化图 | `Visual output/outputs_keyword_cluster.png`、`Visual output/outputs_co_citation_network.png`、`Visual output/outputs_timeline_view.png` | 热点结构、知识基础和前沿如何演变？ |
| Table 1 代表文献表 | `reports/milestone_selection.md`、`reports/claim_evidence_table.csv` | 哪些文献支撑“通用 AI 到半导体场景迁移”的核心判断？ |

补充说明：README 展示多张 CiteSpace 图谱，论文正文写作时应根据 RQ 选择最能服务主线的 3 图 1 表，其余图可作为附录或展示页支撑材料。

---

## 5. 2 分钟 GitHub 闪检讲述路线

| 时间 | 打开位置 | 说什么 |
|---|---|---|
| 0-30 秒 | `README.md` | 项目主题、数据口径、核心发现和快速复现入口 |
| 30-60 秒 | `Data/README.md`、`config/query.yaml`、`baseline/params.md` | 数据来源、检索式、筛选记录、CiteSpace 参数可查 |
| 60-90 秒 | `paper/manuscript_v1.md`、`reports/methods_draft.md` | 论文结构完整，Methods 10 项透明度已覆盖 |
| 90-120 秒 | `Visual output/`、`outputs/`、`docs/引用库与AI伦理说明.md` | 3 图 1 表、交互图、AI 使用说明和最终补件可定位 |

---

## 6. Lesson 27 Top1 整改记录

| 巡检项 | 发现的问题 | 整改动作 | 负责人 | 状态 |
|---|---|---|---|---|
| GitHub 闪检导航 | 现有材料充分，但第 27/28 次课要求分散在多个文件中，老师需要来回找 | 新增本文件，并在课堂进度矩阵、终版归档说明、presentation/reflection 索引中建立入口 | 项目组 | 已完成 |

---

## 7. 第 28 次课复查状态

| 复查项 | 自检结论 | 证据位置 |
|---|---|---|
| 最新 commit | 待提交后更新 GitHub | GitHub commits |
| 核心图表 | 已就位 | `Visual output/`、`outputs/` |
| Methods 透明度 | 10 项已有落点 | `reports/methods_draft.md` |
| 复现说明 | README 提供 `pip install -r requirements.txt` 与 `python run_pipeline.py` | `README.md` |
| 答辩准备 | HTML 主讲材料 + 预答辩准备包 | `项目展示.html`、`docs/预答辩与PR-Review准备包.md` |

当前判断：可进入答辩准备；后续仅需在真实课堂抽签后回填随机序位、课次和现场反馈。

---

## 8. 待真实课堂回填

| 项目 | 待填内容 |
|---|---|
| 随机答辩序位 | 待课堂抽签后填写 |
| 对应答辩课次 | 第 29-32 次课中的具体场次 |
| 教师巡检状态 | 通过 / 需整改 / 高风险 |
| 现场 Top1 整改项 | 若老师提出新问题，记录在此并补 commit 链接 |
| 多成员汇报分工 | 待最终确定主讲与问答成员 |

