---
week: 18
phase: tiny-llm
hardware: [m4-mac]
estimated_hours: 8
status: planned
---

# Week 18：同步 benchmark 与 roofline

## 本周目标

- 正确测量 MLX lazy graph。
- 区分 prefill compute-bound 与 decode bandwidth-bound。

## 实验

固定 warmup、同步、shape、dtype，分别测 prefill 和 decode。

## 交付物

- Week 2 benchmark 报告。

## 验收标准

- [ ] 报告 median 和样本数。
- [ ] 瓶颈判断有数据依据。

## 复盘

- 实际投入：
- 最大困难：
- 尚未解决：

