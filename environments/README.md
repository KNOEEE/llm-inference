# Environments

Do not create one environment containing every dependency. Each directory records setup steps, pinned versions, smoke tests, and the most recent verification date.

| Environment | Purpose |
|---|---|
| cpu-pytorch | Phase 1, CPU tests, and scheduler simulation |
| mac-mlx | Tiny-LLM, MLX, and Metal |
| cuda-triton | CUDA and Triton kernel labs |
| nano-vllm | Independent Nano-vLLM environment |
| vllm | Independent vLLM environment or official container |

After creating an environment, record its actual versions in the corresponding README. Do not guess future-compatible versions now.

