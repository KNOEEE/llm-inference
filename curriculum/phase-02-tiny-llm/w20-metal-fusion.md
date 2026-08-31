---
week: 20
phase: tiny-llm
hardware: [m4-mac]
estimated_hours: 8
status: planned
---

# Week 20：Fused RMSNorm 或 SwiGLU

## 本周目标

- 亲手完成一个有代表性的融合 kernel。
- 建立 oracle→microbench→end-to-end 流程。

## 实验

从 RMSNorm 或 SwiGLU 中选一个实现、测试并接入模型。

## 交付物

- 一个自写 Metal fused op。

## 验收标准

- [ ] 随机和尾部 shape 通过。
- [ ] 完整模型无正确性回退。

## 复盘

- 实际投入：
- 最大困难：
- 尚未解决：

