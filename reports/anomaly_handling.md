# 异常处理说明

> 生成时间：2026-05-08
> 方法：L19 课件要求（同名异义/外部冲击/数据库延迟三类异常）
> 数据来源：DL 纯净集 147 篇，全量集 643 篇

---

## 一、同名异义（Homonym Disambiguation）

### 问题描述

"Transformer" 在 WoS 中同时匹配两种完全不同的含义：

| 含义 | 英文 | 学科 | 典型关键词 |
|------|------|------|-----------|
| 深度学习架构 | Deep Learning Transformer | Computer Science | attention mechanism, vision transformer, ViT, Swin |
| 电力变压器 | Power Transformer | Engineering Electrical | power amplifier, MMIC, DC-DC, Doherty, RF |

### 影响范围

- 全量集 643 篇中，约 496 篇（77%）为电力电子变压器论文
- 若不处理，关键词共现网络会被 "power amplifier"、"Doherty"、"DC-DC" 等电力电子术语主导
- 共被引网络会出现大量电力电子领域文献，干扰知识基础识别

### 处理方法

**DL 语义筛选**：两轮关键词匹配

1. **纳入信号**（任一出现即保留）：
   - attention mechanism, vision transformer, ViT, Swin Transformer, deep learning, neural network, CNN, feature extraction, image classification, defect detection, wafer map

2. **排除信号**（任一出现即排除）：
   - power amplifier, MMIC, DC-DC, Doherty, RF power, voltage, current transformer, power converter, gallium nitride, GaN HEMT

3. **结果**：643 → 147 篇，保留率 22.9%

### 验证

- 筛选后关键词共现网络中无电力电子术语
- 共被引网络核心文献为 Vaswani(2017)、ViT(2021)、Swin(2021)，符合预期
- 详见 reports/screening_rule.md

---

## 二、外部冲击（Exogenous Shocks）

### 问题描述

某些高被引文献并非半导体制造领域内生，而是来自通用 AI 领域的外部知识溢出。

### 识别的外部冲击

| 文献 | 来源领域 | 冲击类型 | 影响 |
|------|----------|----------|------|
| Vaswani(2017) "Attention Is All You Need" | NLP | 跨领域知识溢出 | 奠定 Transformer 架构，中心性 0.2649 |
| Dosovitskiy(2021) ViT | Computer Vision | 跨领域知识溢出 | 打通 CV→制造路径，中心性 0.3452 |
| Liu(2021) Swin Transformer | Computer Vision | 跨领域知识溢出 | 成为晶圆检测最常用 backbone |
| He(2016) ResNet | Computer Vision | 跨领域知识溢出 | 残差连接被 Transformer 吸收 |

### 处理方法

1. **不排除**：这些外部文献是知识基础的核心组成部分，排除会破坏共被引网络结构
2. **标注**：在 Milestone 文献选择表中标注"层级"（L1 架构奠基层 / L2 方法改进层 / L3 应用落地层）
3. **解读**：将外部冲击视为"知识溢出"而非"噪声"，分析传导链（NLP→CV→半导体，约 5 年）

### 传导链

```
Vaswani(2017) → Dosovitskiy(2021) → Liu(2021) → Wei(2022)
    NLP              CV               CV          半导体
  [L1架构层]      [L1架构层]       [L1架构层]   [L3应用层]
```

---

## 三、数据库延迟（Database Lag）

### 问题描述

WoS 数据库存在收录延迟，2025 年数据不完整。

### 影响范围

| 年份 | 全量集发文量 | DL 纯净集发文量 | 完整性评估 |
|------|-------------|----------------|-----------|
| 2023 | ~150 | ~35 | 基本完整 |
| 2024 | ~180 | ~55 | 基本完整 |
| 2025 | ~80 | ~25 | **不完整**（数据导出时间 2025 年中） |

### 处理方法

1. **标注**：在所有涉及 2025 年数据的分析中注明"数据不完整"
2. **谨慎解读**：2025 年突现词（anomaly detection）的强度可能被低估
3. **不外推**：不基于 2025 年数据做趋势外推
4. **时间窗口**：主要分析窗口为 2015-2024，2025 年作为参考

### 对突现检测的影响

- 2025 年突现词的起止年可能不准确（实际起始可能更早）
- 突现强度可能被低估（论文尚未被充分引用）
- anomaly detection 的突现可能比检测到的更强

---

## 四、其他异常

| 异常 | 影响 | 处理 |
|------|------|------|
| WoS 作者字段格式不统一 | 作者数统计困难 | 暂未统计 DL 纯净集作者数 |
| 部分文献无摘要 | DL 语义筛选可能遗漏 | 影响有限（<5%），已在数据质量报告中说明 |
| 自引偏差 | 中心性指标可能偏高 | 影响有限（Q/S 值高，自引对整体结构影响小） |

---

## 总结

| 异常类型 | 严重程度 | 处理状态 | 残余影响 |
|----------|----------|----------|----------|
| Transformer 同名异义 | 高 | ✅ 已处理（643→147） | 无 |
| 外部冲击 | 中 | ✅ 已标注并解读 | 无（视为知识溢出） |
| 数据库延迟 | 中 | ✅ 已标注 | 2025 年数据不完整 |
| 自引偏差 | 低 | ⚠️ 未单独处理 | 影响有限 |
