# 聚类解读三判断

> 生成时间：2026-05-08
> 方法：L19 课件要求（时间线图+时段对比+学科品性 overlay）
> 数据来源：CiteSpace 全量集 643 篇 + DL 纯净集 147 篇

---

## 判断 A：时间线图（Timeline View）

### 方法

在 CiteSpace 中生成聚类时间线图，观察每个聚类的起始时间、活跃时段、跃迁节点。

### 关键发现

| 聚类 | 标签（LLR） | 起始年 | 活跃时段 | 2025 状态 | 解读 |
|------|------------|--------|----------|-----------|------|
| #0 | machine learning | 2020 | 2020-2025 | 活跃 | AI 方法聚类，持续活跃 |
| #1 | annotation | 2021 | 2021-2025 | 活跃 | 数据标注方向，ViT 带动 |
| #2 | defect detection | 2021 | 2021-2025 | 活跃 | 核心应用场景 |
| #3 | wafer map | 2022 | 2022-2025 | 活跃 | 晶圆图分析，2022 起加速 |
| #4 | inductors | 2015 | 2015-2022 | **死亡** | 传统硬件聚类，2022 后无新论文 |
| #8 | cnn | 2020 | 2020-2025 | 活跃 | CNN 仍在使用，但 Transformer 渗透 |
| #9 | parallel processing | 2016 | 2016-2022 | **死亡** | 传统硬件聚类，2022 后系统性退场 |

### 结论

- AI 方向 4 个聚类（#0、#1、#2、#8）全部活跃至 2025
- 传统硬件聚类 #4、#9 于 2022 年后系统性"学术死亡"
- 此消彼长的结构比单纯关键词频次增长更具说服力

---

## 判断 B：时段对比

### 方法

将数据集分为"早期"（2015-2020）和"近期"（2021-2025）两个时段，对比聚类结构变化。

### 早期（2015-2020）

| 特征 | 说明 |
|------|------|
| 主导聚类 | #4 inductors、#9 parallel processing、#6 rf |
| 关键词 | RFID、电感耦合、反激变换器、Doherty |
| 研究范式 | 传统硬件 + 统计方法 |
| Transformer | 无直接应用 |

### 近期（2021-2025）

| 特征 | 说明 |
|------|------|
| 主导聚类 | #0 machine learning、#2 defect detection、#3 wafer map |
| 关键词 | transformers、deep learning、vision transformer、anomaly detection |
| 研究范式 | Transformer + 深度学习 |
| Transformer | 2022 年首篇落地，2024 年全面爆发 |

### 对比结论

| 维度 | 早期 | 近期 | 变化 |
|------|------|------|------|
| 聚类数 | 10 | 10 | 数量不变，内容更替 |
| AI 聚类占比 | 0/10 | 4/10 | 从无到有 |
| 传统硬件聚类 | 4/10 | 0/10 | 全面退场 |
| 发文量 | <20 篇 | >120 篇 | 6 倍增长 |
| 研究范式 | 硬件主导 | AI 主导 | 范式转移 |

---

## 判断 C：学科品性 Overlay

### 方法

在 WoS 学科类别（WC 字段）上做 overlay 分析，识别同一术语在不同学科中的分布。

### Transformer 同名异义问题

| 术语 | 学科 1 | 学科 2 | 处理方法 |
|------|--------|--------|----------|
| Transformer | Computer Science（深度学习） | Engineering Electrical（电力变压器） | DL 语义筛选：保留 attention、vision transformer 等特征词，排除 power amplifier、MMIC、DC-DC 等电力电子术语 |
| CMOS | Engineering Electrical（电路设计） | Physics Applied（器件物理） | 保留，两个学科均与半导体相关 |
| Network | Computer Science（神经网络） | Telecommunications（通信网络） | 根据上下文判断，保留神经网络相关论文 |

### 学科分布（DL 纯净集）

| 学科（WC） | 论文数 | 占比 |
|-----------|--------|------|
| Engineering Electrical Electronic | 58 | 39.5% |
| Computer Science Artificial Intelligence | 42 | 28.6% |
| Computer Science Interdisciplinary Applications | 31 | 21.1% |
| Engineering Manufacturing | 24 | 16.3% |
| Instruments Instrumentation | 18 | 12.2% |

### 学科品性陷阱识别

| 陷阱 | 表现 | 处理 |
|------|------|------|
| Transformer 同名异义 | 643 篇中 496 篇为电力电子 | DL 语义筛选 643→147 |
| CMOS 跨学科 | 电路设计 vs 器件物理 | 保留，均与半导体相关 |
| Network 歧义 | 神经网络 vs 通信网络 | 根据上下文判断 |

### 结论

- **Transformer 同名异义是本领域最大的学科品性陷阱**，必须在数据清洗阶段处理
- DL 语义筛选（643→147）有效排除了 77% 的噪声
- 学科分布显示本领域是"电气工程+AI+制造"的交叉学科

---

## 三判断综合结论

1. **时间线判断**：AI 聚类活跃至 2025，传统硬件聚类 2022 后死亡，此消彼长结构清晰
2. **时段对比判断**：早期硬件主导→近期 AI 主导，范式转移完成
3. **学科品性判断**：Transformer 同名异义是最大陷阱，DL 语义筛选有效处理

> **原则**：聚类解读 = "活" + "核"。"活"看时间线，"核"看中心性。本领域 AI 聚类"活"至 2025，ViT/Transformer 是"核"心节点。
