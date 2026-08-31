# RMSNorm Cross-backend Lab

建议贯穿 W08、W20、W35 和 W38。

固定协议：

- 输入 shape 至少覆盖 decode 和 prefill 场景；
- FP16/BF16 输入使用 FP32 accumulate；
- PyTorch FP32 实现作为 oracle；
- 所有后端使用相同随机种子、epsilon 和误差阈值；
- microbenchmark 与端到端结果分开报告。

