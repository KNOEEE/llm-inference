# Kernel Lab

用同一个 correctness harness 比较 PyTorch/MLX/Metal/CUDA/Triton。推荐只完整跨后端复刻一个代表性算子，例如 RMSNorm。

每个算子目录应包含：

```text
README.md
torch_reference.py
mlx_impl.py
metal/
cuda/
triton_impl.py
test_correctness.py
bench.py
results/
```

不要为了填目录而提前创建空实现。

