---
week: 6
phase: foundations
hardware: [cpu-linux, m4-mac]
estimated_hours: 8
status: planned
---

# Week 06：Embedding、Linear、softmax 与 causal mask

## 本周目标

- 理解 token 到 Q/K/V 的数据流。
- 实现数值稳定 softmax 和 causal mask。

## 实验

不用 `nn.Transformer` 组装 attention 的输入路径。

## 交付物

- attention 输入流水线。

## 验收标准

- [ ] mask 没有 off-by-one。
- [ ] 极大 logits 下 softmax 不溢出。

## 复盘

- 实际投入：
- 最大困难：
- 尚未解决：

