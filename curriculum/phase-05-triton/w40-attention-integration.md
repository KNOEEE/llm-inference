---
week: 40
phase: triton
hardware: [nvidia-linux]
estimated_hours: 8
status: planned
---

# Week 40：Fused attention 与模型接入

## 本周目标

- 理解 online softmax 和 causal tiling。
- 把至少一个 Triton op 接入 Qwen 路径。

## 实验

阅读 fused attention，实现或修改教学版本，并完成端到端 logits 回归。

## 交付物

- Triton 集成阶段报告。

## 验收标准

- [ ] 端到端结果在容差内。
- [ ] 异常 shape 自动 fallback。

## 复盘

- 实际投入：
- 最大困难：
- 尚未解决：

