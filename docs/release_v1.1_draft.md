# Release v1.1 草案

> 拟发布时间：第十四周收尾后
> 用途：替换当前 `v1.0` 与 `main` 分支之间的对外信息落差

## 建议标题

`v1.1 - Week 14 consistency and reproducibility refresh`

## 建议正文

### What changed

- 对外主叙事统一到 2015-2025 时间范围与双数据集口径
- README、论文初稿、进度文档同步反映 2026-05-16 后的写作模块补齐状态
- 修复本地复现链中的口径风险：`create_screening.py` 与 `burst_detection.py` 默认仅读取全量主数据集 643 篇，不再误混 `download_1-147.txt`
- Python 依赖说明补齐：新增 `scipy`、`matplotlib`、`pyvis`

### Data scope

- 全量集：643 篇，用于国家/机构分布与宏观统计
- DL 纯净集：147 篇，用于 CiteSpace 图谱与 Python 网络分析

### Why this release matters

`v1.0` 已能展示项目主体成果，但其发布时间为 2026-05-01，仍早于双数据集口径统一、L21-L22 写作补齐和第十四周复现链核查。本次版本的目标不是推翻已有成果，而是让仓库首页、GitHub Pages、Release 描述与本地运行逻辑重新保持一致。

### Suggested quick check

```bash
pip install -r requirements.txt
python run_pipeline.py
node run_pipeline.js
```
