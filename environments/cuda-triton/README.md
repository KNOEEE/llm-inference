# CUDA / Triton Environment

Use this environment for CUDA extensions, Triton, and kernel profiling. Pin the GPU model, driver, CUDA toolkit, PyTorch, Triton, and compute capability.

The smoke test must include:

```bash
nvidia-smi
nvcc --version
python -c 'import torch; print(torch.cuda.is_available(), torch.cuda.get_device_name())'
```

Validate FlashAttention in the Nano-vLLM environment; it is not a prerequisite for the first CUDA labs.

