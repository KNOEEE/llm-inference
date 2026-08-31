# 52 周路线图

时间是建议值，不是截止日期。每一阶段通过验收后再进入下一阶段。

| 周 | 主题 | 主要设备 | 核心交付物 |
|---:|---|---|---|
| 01 | Tensor、shape、dtype、device | CPU/M4 | Tensor 观察实验 |
| 02 | 广播、stride、view、contiguous | CPU/M4 | 非连续 Tensor 测试 |
| 03 | Module、Parameter、state_dict | CPU/M4 | 可保存的小模块 |
| 04 | Autograd 与最小训练循环 | CPU/M4 | 过拟合 tiny dataset |
| 05 | 数值正确性、pytest、profiler | CPU/M4 | 测试与性能基线 |
| 06 | Embedding、Linear、softmax、mask | CPU/M4 | attention 输入流水线 |
| 07 | MHA 与 GQA | CPU/M4 | 纯 PyTorch attention |
| 08 | RoPE、RMSNorm、SwiGLU | CPU/M4 | 三个基础算子 |
| 09 | Decoder block 与采样 | CPU/M4 | 一层 decoder |
| 10 | Naive decode 与 KV cache toy | CPU/M4 | cache 前后对照 |
| 11 | MLX 与 Tiny-LLM 环境 | M4 | Qwen3-0.6B baseline |
| 12 | Tiny-LLM attention | M4 | Week 1 attention |
| 13 | Tiny-LLM RoPE 与 GQA | M4 | 位置和 head 对齐 |
| 14 | Tiny-LLM RMSNorm 与 MLP | M4 | Transformer block 组件 |
| 15 | Qwen3 block 与完整模型 | M4 | 模型前向 |
| 16 | 权重加载、generation、Week 1 验收 | M4 | 可读版推理器 |
| 17 | Dense KV cache | M4 | cache 正确性对照 |
| 18 | 同步 benchmark 与 roofline | M4 | prefill/decode 报告 |
| 19 | Metal 执行模型与 reduction | M4 | Metal 入门实验 |
| 20 | Fused RMSNorm 或 SwiGLU | M4 | 一个自写 Metal kernel |
| 21 | W4A16/Decode attention 阅读与 off-ramp | M4 | 算子取舍记录 |
| 22 | Tiny-LLM Week 2 集成与验收 | M4 | 单请求优化报告 |
| 23 | Continuous batching | M4 | 多请求时间线 |
| 24 | Chunked prefill 与公平性 | M4 | 调度 trace |
| 25 | Paged KV allocator | M4/CPU | BlockManager 测试 |
| 26 | Direct paged attention | M4 | dense/paged 对照 |
| 27 | Paged prefill 与系统测量 | M4 | serving 指标报告 |
| 28 | Tiny-LLM Week 3 验收 | M4 | mini serving engine |
| 29 | 环境锁定、测试和仓库规范 | CPU Linux | 可复现入口 |
| 30 | OpenAI-like API 与异步执行 | CPU Linux | 本地 API |
| 31 | Load generator 与指标 | CPU Linux | 固定 workload 压测 |
| 32 | 实验报告与 NVIDIA 入场检查 | CPU/NVIDIA | GPU readiness 报告 |
| 33 | CUDA 执行模型与 vector add | NVIDIA | 第一个 CUDA kernel |
| 34 | 合并访存、shared memory、reduction | NVIDIA | reduction 对照 |
| 35 | Tiled matmul 与 RMSNorm | NVIDIA | 两类 kernel 实验 |
| 36 | Nsight、sanitizer 与 Metal 映射 | NVIDIA | CUDA 阶段报告 |
| 37 | Triton program、block、mask | NVIDIA | Triton vector add |
| 38 | Fused softmax 与 RMSNorm | NVIDIA | reduction kernel |
| 39 | Matmul、autotune 与 shape dispatch | NVIDIA | 多 shape benchmark |
| 40 | Fused attention 与模型接入 | NVIDIA | Triton 集成报告 |
| 41 | Nano-vLLM 运行与模型层 | NVIDIA | Qwen3-0.6B eager baseline |
| 42 | Sequence、BlockManager、Scheduler | NVIDIA | 状态机 trace |
| 43 | ModelRunner、KV scatter、attention | NVIDIA | 请求调用链 |
| 44 | Prefix cache、CUDA Graph、preemption | NVIDIA | Nano-vLLM 实验报告 |
| 45 | vLLM offline 与 API server | NVIDIA | 两种入口 baseline |
| 46 | EngineCore、Worker、ModelRunner | NVIDIA | 一条请求架构图 |
| 47 | 调度、KV、并发度与 SLO | NVIDIA | 参数 sweep |
| 48 | Nano-vLLM 与 vLLM 对照 | NVIDIA | 公平比较报告 |
| 49 | 毕业项目提案与 baseline | 全部 | 实验设计文档 |
| 50 | 实现、测试与 instrumentation | 全部 | 可测功能 |
| 51 | 实验矩阵、消融与失败分析 | NVIDIA | 原始结果和结论 |
| 52 | 报告、演示与复现验收 | 全部 | 完整毕业项目 |

## 可选专题

完成主线后只选择一个深入：完整 Tiny-LLM Metal Week 2、tensor parallel、speculative decoding、MoE、prefix-aware scheduling 或 vLLM 源码贡献。

