# RMSNorm Cross-backend Lab

This lab spans W08, W20, W35, and W38.

Fixed protocol:

- cover both decode and prefill input shapes;
- use FP32 accumulation for FP16/BF16 inputs;
- use the PyTorch FP32 implementation as the oracle;
- use the same seed, epsilon, and error threshold for every backend;
- report microbenchmarks separately from end-to-end results.

