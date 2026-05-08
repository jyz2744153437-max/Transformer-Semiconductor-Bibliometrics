# 学科品性陷阱识别与处理

> 生成时间：2026-05-08
> 方法：L20 课件要求
> 数据来源：DL 纯净集 147 篇，全量集 643 篇

---

## 什么是学科品性陷阱？

同一术语在不同学科中含义完全不同，如果直接做关键词共现分析，会把不同学科的论文错误地聚在一起，产生虚假聚类。

---

## 本领域识别的学科品性陷阱

### 陷阱 1：Transformer 同名异义（严重度：高）

| 含义 | 学科 | 典型关键词 | 论文数 |
|------|------|-----------|--------|
| 深度学习架构 | Computer Science / AI | attention, ViT, Swin, feature extraction | 147 |
| 电力变压器 | Engineering Electrical | power amplifier, MMIC, DC-DC, Doherty | 496 |

**处理**：DL 语义筛选（643→147），详见 reports/anomaly_handling.md

**如果不处理会怎样**：关键词共现网络会出现 "transformer ↔ power amplifier ↔ Doherty" 的虚假聚类，完全偏离研究主题。

---

### 陷阱 2：Network 歧义（严重度：中）

| 含义 | 学科 | 典型关键词 |
|------|------|-----------|
| 神经网络 | Computer Science / AI | neural network, deep learning, CNN |
| 通信网络 | Telecommunications | 5G, IoT, sensor network |

**处理**：在 DL 语义筛选中，"neural network" 作为纳入信号，"sensor network" 不在排除词表中但也不会被纳入（因为缺乏 DL 特征词）。

**影响**：147 篇中未发现通信网络论文，影响可忽略。

---

### 陷阱 3：CMOS 跨学科（严重度：低）

| 含义 | 学科 | 典型关键词 |
|------|------|-----------|
| CMOS 电路设计 | Engineering Electrical | CMOS circuit, logic gate, VLSI |
| CMOS 器件物理 | Physics Applied | CMOS process, finFET, scaling |

**处理**：两个学科均与半导体相关，保留所有 CMOS 论文。

**影响**：无虚假聚类风险。

---

### 陷阱 4：Classification 歧义（严重度：低）

| 含义 | 学科 | 典型关键词 |
|------|------|-----------|
| 图像分类 | Computer Vision | image classification, CNN, feature |
| 文本分类 | NLP | text classification, sentiment analysis |

**处理**：检索式中 NOT TS=("NLP" OR "natural language") 已排除 NLP 论文。

**影响**：147 篇中未发现文本分类论文。

---

## 处理效果验证

| 指标 | 处理前（643 篇） | 处理后（147 篇） |
|------|-----------------|-----------------|
| 电力电子术语 | 大量（Doherty、MMIC、DC-DC） | 0 |
| 关键词聚类 Q 值 | ~0.4（噪声干扰） | 0.673 |
| 关键词聚类 S 值 | ~0.5 | 0.902 |
| 聚类可解读性 | 低（混合聚类） | 高（语义清晰） |

---

## 经验总结

1. **同名异义是文献计量最常见的陷阱**，尤其在跨学科检索中
2. **处理时机**：数据清洗阶段，而非分析后
3. **验证方法**：检查聚类标签是否语义一致，Q/S 值是否显著
4. **文档化**：筛选规则必须记录，确保可复现
