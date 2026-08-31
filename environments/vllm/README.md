# vLLM Environment

建议固定 release 或官方容器，不追随 master。记录镜像 digest/版本、GPU、driver、模型、完整启动参数和 benchmark command。

不要复用 Nano-vLLM 环境，避免 PyTorch/Triton/FlashAttention 二进制依赖冲突。

