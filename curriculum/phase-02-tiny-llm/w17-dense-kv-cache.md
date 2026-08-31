---
week: 17
phase: tiny-llm
hardware: [m4-mac]
estimated_hours: 8
status: planned
---

# Week 17：Dense KV cache

## 本周目标

- 让每层 cache 归属于请求。
- 正确处理 position 与 append。

## 实验

实现 cache 并在多个 prompt/output 长度下比较开关结果。

## 交付物

- dense KV cache 实现。

## 验收标准

- [ ] cache 前后 greedy 输出一致。
- [ ] decode 不再重算旧 K/V。

## 复盘

- 实际投入：
- 最大困难：
- 尚未解决：

