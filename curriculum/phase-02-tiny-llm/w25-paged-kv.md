---
week: 25
phase: tiny-llm
hardware: [m4-mac]
estimated_hours: 8
status: planned
---

# Week 25：Paged KV allocator

## 本周目标

- 理解逻辑 block 与物理 page。
- 实现分配、释放和复用 invariant。

## 实验

在 CPU scripted model 上缩小 page pool，强制触发边界情况。

## 交付物

- BlockManager 状态机测试。

## 验收标准

- [ ] 无泄漏和重复释放。
- [ ] 可以预测每一步 block table。

## 复盘

- 实际投入：
- 最大困难：
- 尚未解决：

