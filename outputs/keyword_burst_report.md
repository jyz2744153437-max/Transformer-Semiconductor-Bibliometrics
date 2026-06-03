# 关键词突现检测报告

> 基于 Kleinberg 突现检测算法（Python 复核口径）
> 创建日期：2026-06-03

---

## 1. 突现检测方法

> 说明：本报告基于 `src/burst_detection.py` 对 **DL 纯净集 147 篇** 的本地 Python 复核结果生成，主要用于趋势辅助核对。正式答辩口径中的突现词数量仍以 CiteSpace 导出结果为准。

| 项目 | 说明 |
|---|---|
| 算法 | Kleinberg Burst Detection |
| 参数 | s=2, γ=1 |
| 最小频次 | 5 |
| Python 复核结果 | 17 个突现 |
| 正式答辩口径 | CiteSpace 突现图谱（DL 纯净集 147 篇） |

---

## 2. 突现时间分布

### 2015-2018 (早期)

| 关键词 | 突现区间 | 强度 | 总频次 |
|---|---|---|---|
| integrated | 2017-2017 | 1 | 6 |

### 2019-2022 (中期)

*无突现*

### 2023-2025 (近期)

| 关键词 | 突现区间 | 强度 | 总频次 |
|---|---|---|---|
| deep learning | 2024-2025 | 2 | 33 |
| transformer | 2024-2025 | 2 | 34 |
| integrated circuit modeling | 2024-2025 | 1 | 19 |
| manufacturing | 2024-2024 | 1 | 5 |
| integrated circuit | 2024-2025 | 1 | 8 |
| vision transformer | 2025-2025 | 1 | 11 |
| network | 2025-2025 | 1 | 12 |
| anomaly detection | 2025-2025 | 1 | 8 |
| transformers | 2025-2025 | 1 | 29 |
| data models | 2025-2025 | 1 | 8 |
| computational modeling | 2025-2025 | 1 | 11 |
| semiconductor manufacturing | 2025-2025 | 1 | 11 |
| feature extraction | 2025-2025 | 1 | 13 |
| deep | 2025-2025 | 1 | 6 |
| learning | 2025-2025 | 1 | 8 |
| accuracy | 2025-2025 | 1 | 17 |

---

## 3. Top 20 突现关键词（按原始检测结果排序）

| 排名 | 关键词 | 突现区间 | 强度 | 总频次 |
|---|---|---|---|---|
| 1 | deep learning | 2024-2025 | 2 | 33 |
| 2 | transformer | 2024-2025 | 2 | 34 |
| 3 | integrated | 2017-2017 | 1 | 6 |
| 4 | integrated circuit modeling | 2024-2025 | 1 | 19 |
| 5 | manufacturing | 2024-2024 | 1 | 5 |
| 6 | integrated circuit | 2024-2025 | 1 | 8 |
| 7 | vision transformer | 2025-2025 | 1 | 11 |
| 8 | network | 2025-2025 | 1 | 12 |
| 9 | anomaly detection | 2025-2025 | 1 | 8 |
| 10 | transformers | 2025-2025 | 1 | 29 |
| 11 | data models | 2025-2025 | 1 | 8 |
| 12 | computational modeling | 2025-2025 | 1 | 11 |
| 13 | semiconductor manufacturing | 2025-2025 | 1 | 11 |
| 14 | feature extraction | 2025-2025 | 1 | 13 |
| 15 | deep | 2025-2025 | 1 | 6 |
| 16 | learning | 2025-2025 | 1 | 8 |
| 17 | accuracy | 2025-2025 | 1 | 17 |

---

## 4. 突现解读

### 4.1 早期突现 (2015-2018)

以电力电子、射频器件相关术语为主，反映了半导体器件设计领域的传统热点。

### 4.2 中期突现 (2019-2022)

器件建模、磁性材料等主题出现突现，显示半导体建模方法的演进。

### 4.3 近期突现 (2023-2025)

**Transformer、deep learning、vision transformer** 等深度学习术语突现，表明 Transformer 架构在半导体领域的研究在 2023 年后进入爆发期。

说明：课程展示页与论文正文采用 CiteSpace 正式图谱结果；本报告仅说明 Python 复核得到的方向性信号。

关键发现：
- `transformers` 在 2023-2025 突现，强度 2，总频次 76
- `deep learning` 在 2024-2025 突现，强度 2，总频次 37
- `vision transformer` 在 2025 突现，强度 1，总频次 12

---

**文档版本**：v1.1 draft
**创建日期**：2026-06-03
