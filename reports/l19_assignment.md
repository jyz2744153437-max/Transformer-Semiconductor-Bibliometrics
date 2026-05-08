# L19 作业：发文趋势图 + 指标解读 + 基准文献清单

> 生成时间：2026-05-08
> 课程：文献计量学 L19
> 选题：发文趋势 + 突现检测

---

## 1. 图谱

**选用图谱**：突现检测时间线图

**文件**：`Visual output/outputs_burst_timeline.png`

**图谱说明**：Kleinberg 突现检测算法识别 25 个突现词，红色区间为突现活跃期。2024 年 6 词同步突现（vision transformers、ViT、SEM、super resolution、load modeling、data augmentation），标志领域进入爆发期。2025 年 anomaly detection 接棒，前沿从"已知分类"→"未知检测"升级。

---

## 2. 指标解读（200 字）

**突现强度（Burst Strength）**衡量关键词在短时间内被密集使用的程度。本领域 25 个突现词中，transformers(2.0, 2023-2025) 和 classification(1.90, 2022-2024) 强度最高，反映 Transformer 方法在 2023 年后的爆发式渗透。2024 年 6 词同步突现是关键拐点——vision transformers(1.60)、ViT(1.50) 等术语同时出现，说明领域从"方法迁移"进入"场景落地"阶段。2025 年 anomaly detection(1.30) 接棒，标志前沿从"已知缺陷分类"向"未知异常检测"升级。早期突现词（RFID、inductors）均为传统硬件术语，2022 年后系统性退场，与 AI 术语的此消彼长构成完整的三阶段技术演进。

---

## 3. 基准文献清单（10 篇）

| # | 文献 | 中心性 | 加权度 | Sigma | 选择理由 |
|---|------|--------|--------|-------|----------|
| 1 | Vaswani A et al. (2017) Attention Is All You Need, NeurIPS | 0.2649 | 68 | 0.5514 | Transformer 原始论文，注意力机制奠基 |
| 2 | Dosovitskiy A et al. (2021) An Image is Worth 16x16 Words, Arxiv | 0.3452 | 156 | 1.3452 | ViT 开山之作，中心性全场最高 |
| 3 | Liu Z et al. (2021) Swin Transformer, ICCV | 0.1277 | 67 | 0.4844 | 层级窗口注意力，晶圆检测最常用 backbone |
| 4 | He KM et al. (2016) Deep Residual Learning, CVPR | 0.0718 | 79 | 0.5428 | ResNet 残差连接被 Transformer 吸收 |
| 5 | Wei YX et al. (2022) Mixed-type Wafer Defect Recognition with Transformer, IEEE TSM | 0.0000 | 28 | 0.1795 | 首篇 Transformer 晶圆缺陷识别，落地拐点 |
| 6 | Fan SKS et al. (2024) ViT-based Wafer Map Classification, IJPE | — | — | — | ViT 晶圆图分类 SOTA，TRL 5 代表 |
| 7 | Chen KQ et al. (2023) Multi-scale GAN with Transformer, ESWA | — | — | — | Transformer+GAN 融合，多尺度检测 |
| 8 | Carion N et al. (2020) DETR, ECCV | — | — | — | 端到端目标检测，方法改进层核心 |
| 9 | Touvron H et al. (2021) DeiT, ICML | — | — | — | 数据高效的 ViT 训练，降低落地门槛 |
| 10 | Wang JR et al. (2020) Deep Learning in Semiconductor Manufacturing, IEEE TSM | 0.0058 | 64 | 0.4126 | 半导体 DL 综述，领域内引用最高 |

> 注：#6-#9 的中心性/加权度/Sigma 值为 CiteSpace 共被引网络指标，需从 CiteSpace 软件导出。此处标注"—"表示 Python 管道未单独计算该文献指标（因共被引网络节点为引用文献而非施引文献）。
