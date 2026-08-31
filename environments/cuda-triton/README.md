# CUDA / Triton Environment

用于 CUDA extension、Triton 和 kernel profiling。固定 GPU、driver、CUDA toolkit、PyTorch、Triton 和 compute capability。

Smoke test 至少包含：

```bash
nvidia-smi
nvcc --version
python -c 'import torch; print(torch.cuda.is_available(), torch.cuda.get_device_name())'
```

FlashAttention 安装放在 Nano-vLLM 环境验证，不作为最初 CUDA lab 的前置。

