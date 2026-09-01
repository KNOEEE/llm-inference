# Toy Transformer

A pure PyTorch decoder-only model that evolves from W06 onward.

Suggested structure:

```text
src/
tests/
benchmarks/
README.md
```

Start with FP32 CPU only. Add MPS or BF16 only after shape and numerical tests pass. By W10, support a deterministic comparison between naive decoding and KV-cache decoding.

