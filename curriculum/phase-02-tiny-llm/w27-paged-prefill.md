---
week: 27
phase: tiny-llm
hardware: [m4-mac]
estimated_hours: 8
status: planned
---

# Week 27：Paged prefill 与系统测量

## 本周目标

- 理解长 query 的 page-aware attention。
- 建立 serving 指标。

## 实验

完成不同 prompt、并发度和 page pool 大小的 sweep。

## 交付物

- TTFT/TPOT/吞吐/KV 报告。

## 验收标准

- [ ] 同时报告延迟与吞吐。
- [ ] 不把单请求变慢误判为系统失败。

## 复盘

- 实际投入：
- 最大困难：
- 尚未解决：

