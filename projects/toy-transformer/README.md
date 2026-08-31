# Toy Transformer

从 W06 开始演进的纯 PyTorch decoder-only 模型。

建议结构：

```text
src/
tests/
benchmarks/
README.md
```

最初只实现 FP32 CPU；通过 shape 和数值测试后再考虑 MPS/BF16。W10 应支持 naive decode 与 KV-cache decode 的确定性对照。

