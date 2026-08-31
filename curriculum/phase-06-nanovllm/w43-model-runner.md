---
week: 43
phase: nanovllm
hardware: [nvidia-linux]
estimated_hours: 8
status: planned
---

# Week 43：ModelRunner、KV scatter 与 attention

## 本周目标

- 追踪 batch metadata 到 kernel。
- 区分 prefill/decode attention 路径。

## 实验

沿一条请求记录 slot mapping、KV store、FlashAttention 和 sampler。

## 交付物

- 完整请求调用链。

## 验收标准

- [ ] 能指出 PyTorch/Triton/FlashAttention 分工。
- [ ] trace 可关联 sequence 与物理 slot。

## 复盘

- 实际投入：
- 最大困难：
- 尚未解决：

