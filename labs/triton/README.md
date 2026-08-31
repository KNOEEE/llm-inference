# Triton Labs

对应 W37–W40。建议顺序：vector add → fused softmax → RMSNorm → matmul → fused attention。

记录首次 JIT 与稳态延迟，覆盖尾块、非 2 次幂和异常 stride；不能只保留最快的 shape。

