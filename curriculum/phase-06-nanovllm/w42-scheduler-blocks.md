---
week: 42
phase: nanovllm
hardware: [nvidia-linux]
estimated_hours: 8
status: planned
---

# Week 42：Sequence、BlockManager 与 Scheduler

## 本周目标

- 理解 waiting/running、token budget 和 preemption。
- 追踪 block 分配与 prefix hash。

## 实验

加入结构化 trace，并对分配、引用计数、释放写测试。

## 交付物

- scheduler/block trace。

## 验收标准

- [ ] 能在纸上预测一次 schedule。
- [ ] 无 block 生命周期疑点。

## 复盘

- 实际投入：
- 最大困难：
- 尚未解决：

