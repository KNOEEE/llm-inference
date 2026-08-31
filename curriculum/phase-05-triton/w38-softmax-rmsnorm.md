---
week: 38
phase: triton
hardware: [nvidia-linux]
estimated_hours: 8
status: planned
---

# Week 38：Fused softmax 与 RMSNorm

## 本周目标

- 学习 reduction 和数值稳定性。
- 复刻 CUDA/Metal RMSNorm 对照。

## 实验

实现 fused softmax 和 inference-only RMSNorm。

## 交付物

- 两个 Triton reduction kernel。

## 验收标准

- [ ] 与 PyTorch oracle 对齐。
- [ ] 测试非 2 次幂和大值输入。

## 复盘

- 实际投入：
- 最大困难：
- 尚未解决：

