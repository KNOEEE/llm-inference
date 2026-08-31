# Serving Benchmark

为 Tiny-LLM、Nano-vLLM 和 vLLM 提供一致的 workload 与指标口径。

至少支持：

- 固定 prompt/output 长度；
- 混合长短请求；
- 并发度 sweep；
- 共享前缀比例；
- TTFT、TPOT、request/token throughput、p50/p95、错误率。

