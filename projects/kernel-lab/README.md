# Kernel Lab

Use one correctness harness to compare PyTorch, MLX, Metal, CUDA, and Triton. Fully port only one representative operator across all backends, such as RMSNorm.

Each operator directory should eventually contain:

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

Do not create empty implementations merely to fill the directory.

