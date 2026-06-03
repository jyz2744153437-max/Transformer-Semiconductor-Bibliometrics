# Release v1.1 草案

> 拟发布时间：2026-06-03 之后
> 用途：承接 `v1.0`，将项目推进到“答辩收口 + 课程补件对齐 + 复现链修复”的公开版本

## 建议标题

`v1.1 - Defense-ready consistency and reproducibility refresh`

## 建议正文

### What changed

- 对外主叙事统一到 2015-2025 时间范围与双数据集口径
- README、论文初稿、进度文档同步反映 2026-05-16 后的写作模块补齐状态
- 修复本地复现链中的口径风险：`create_screening.py` 与 `burst_detection.py` 默认仅读取全量主数据集 643 篇，不再误混 `download_1-147.txt`
- Python 依赖说明补齐：新增 `scipy`、`matplotlib`、`pyvis`
- 新增课堂第 21-32 次课对照矩阵、AI/伦理说明、智能体工作流、写作修订日志、预答辩准备包与终版归档说明
- 将 `项目展示.html` 从“成果展示页”升级为“答辩主舞台”，新增总论点、证据链、里程碑文献与技术路线综合页面

### Data scope

- 全量集：643 篇，用于国家/机构分布与宏观统计
- DL 纯净集：147 篇，用于 CiteSpace 图谱与 Python 网络分析

### Why this release matters

`v1.0` 已能展示项目主体成果，但其发布时间为 2026-05-01，仍早于双数据集口径统一、L21-L22 写作补齐和第十四周复现链核查，也尚未把课堂第 21-32 次课要求整理成老师可直接检查的入口。本次版本的目标不是推翻已有成果，而是让仓库首页、GitHub Pages、课程补件、Release 描述与本地运行逻辑重新保持一致，并把 HTML 页面提升为真正可独立答辩的主材料。

### Public-facing highlights

- HTML 页面现在不仅展示结果，还提前给出总论点，并用证据链、里程碑文献与技术路线页形成更完整的学术叙事
- 课程过程产物不再散落在底稿中，而是通过统一文档入口进行组织
- 本地复现链与公开叙事都回到相同口径：`2015-2025`、`643 / 147`

### Suggested quick check

```bash
pip install -r requirements.txt
python run_pipeline.py
node run_pipeline.js
```
