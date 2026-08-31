---
week: 26
phase: tiny-llm
hardware: [m4-mac]
estimated_hours: 8
status: planned
---

# Week 26：Direct paged attention

## 本周目标

- 让 attention 直接读取非连续 KV page。
- 避免先 gather 为 dense cache。

## 实验

对同一请求比较 dense、paged-gather 和 direct-paged 输出。

## 交付物

- direct paged attention 实现。

## 验收标准

- [ ] 三条路径结果在容差内。
- [ ] 确认热路径没有 dense rebuild。

## 复盘

- 实际投入：
- 最大困难：
- 尚未解决：

