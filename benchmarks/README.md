# Benchmark Protocol

性能结果必须同时具备正确性和可复现性。

## 必记字段

- 仓库 commit、依赖版本、设备与驱动；
- 模型、权重格式、dtype、采样参数；
- prompt/output 长度、batch/concurrency；
- warmup、同步方式、样本数；
- TTFT、TPOT、吞吐、p50/p95、显存和失败率。

## 约束

- 不比较不同权重格式后的逐 token bit equality。
- 不把首次编译时间混入稳态 kernel latency。
- 不用 Mac 与 NVIDIA 的绝对吞吐判断后端优劣。
- 原始结果遵循 `schemas/result.schema.json`；大文件进入 `artifacts/`。

