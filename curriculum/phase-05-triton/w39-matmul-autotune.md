---
week: 39
phase: triton
hardware: [nvidia-linux]
estimated_hours: 8
status: planned
---

# Week 39：Matmul、autotune 与 shape dispatch

## 本周目标

- 理解 block matmul、L2 friendly 排序和 autotune。
- 避免动态 shape 编译爆炸。

## 实验

基于官方教程做有限配置 sweep，并增加 fallback guard。

## 交付物

- 多 shape matmul 报告。

## 验收标准

- [ ] 不把编译时间算入稳态。
- [ ] 性能结论不只选赢家 shape。

## 复盘

- 实际投入：
- 最大困难：
- 尚未解决：

