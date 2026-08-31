# Environments

不要建立一个包含所有依赖的环境。每个目录记录创建方式、锁定版本、smoke test 和最后验证日期。

| 环境 | 用途 |
|---|---|
| cpu-pytorch | Phase 1、CPU 测试和调度模拟 |
| mac-mlx | Tiny-LLM、MLX、Metal |
| cuda-triton | CUDA/Triton kernel lab |
| nano-vllm | Nano-vLLM 独立环境 |
| vllm | vLLM 独立环境或官方容器 |

环境建立后，将真实版本写回对应 README；不要现在猜测未来兼容版本。

