# CUDA Labs

对应 W33–W36。每个 kernel 至少包含 PyTorch reference、CUDA 实现、边界测试和 benchmark。

建议顺序：vector add → reduction → RMSNorm → tiled matmul。所有测试先跑 compute-sanitizer，再做性能分析。

