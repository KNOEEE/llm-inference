# 52-Week Roadmap

The schedule is a recommendation, not a deadline. Advance only after meeting each phase's acceptance criteria.

| Week | Topic | Primary hardware | Core deliverable |
|---:|---|---|---|
| 01 | Tensors, shapes, dtypes, and devices | CPU/M4 | Tensor observation lab |
| 02 | Broadcasting, strides, views, and contiguity | CPU/M4 | Non-contiguous tensor tests |
| 03 | Modules, parameters, and state dictionaries | CPU/M4 | A saveable module |
| 04 | Autograd and a minimal training loop | CPU/M4 | Overfit a tiny dataset |
| 05 | Numerical correctness, pytest, and profiling | CPU/M4 | Tests and performance baseline |
| 06 | Embeddings, linear layers, softmax, and masks | CPU/M4 | Attention input pipeline |
| 07 | MHA and GQA | CPU/M4 | Pure PyTorch attention |
| 08 | RoPE, RMSNorm, and SwiGLU | CPU/M4 | Three core operators |
| 09 | Decoder block and sampling | CPU/M4 | One decoder layer |
| 10 | Naive decoding and a toy KV cache | CPU/M4 | Cache comparison |
| 11 | MLX and the Tiny-LLM environment | M4 | Qwen3-0.6B baseline |
| 12 | Tiny-LLM attention | M4 | Week 1 attention |
| 13 | Tiny-LLM RoPE and GQA | M4 | Position and head alignment |
| 14 | Tiny-LLM RMSNorm and MLP | M4 | Transformer block components |
| 15 | Qwen3 block and complete model | M4 | Model forward pass |
| 16 | Weight loading, generation, and Week 1 review | M4 | Readable inference engine |
| 17 | Dense KV cache | M4 | Cache correctness comparison |
| 18 | Synchronized benchmarks and roofline analysis | M4 | Prefill/decode report |
| 19 | Metal execution model and reductions | M4 | Introductory Metal lab |
| 20 | Fused RMSNorm or SwiGLU | M4 | One custom Metal kernel |
| 21 | W4A16/decode attention study and operator off-ramp | M4 | Operator trade-off record |
| 22 | Tiny-LLM Week 2 integration and review | M4 | Single-request optimization report |
| 23 | Continuous batching | M4 | Multi-request timeline |
| 24 | Chunked prefill and fairness | M4 | Scheduling trace |
| 25 | Paged KV allocator | M4/CPU | BlockManager tests |
| 26 | Direct paged attention | M4 | Dense/paged comparison |
| 27 | Paged prefill and system measurement | M4 | Serving metrics report |
| 28 | Tiny-LLM Week 3 review | M4 | Mini serving engine |
| 29 | Environment locking, tests, and repository conventions | CPU Linux | Reproducible entry point |
| 30 | OpenAI-like API and asynchronous execution | CPU Linux | Local API |
| 31 | Load generator and metrics | CPU Linux | Fixed-workload load test |
| 32 | Experiment reporting and NVIDIA readiness | CPU/NVIDIA | GPU readiness report |
| 33 | CUDA execution model and vector addition | NVIDIA | First CUDA kernel |
| 34 | Coalesced access, shared memory, and reductions | NVIDIA | Reduction comparison |
| 35 | Tiled matrix multiplication and RMSNorm | NVIDIA | Two kernel labs |
| 36 | Nsight, sanitizers, and Metal mapping | NVIDIA | CUDA phase report |
| 37 | Triton programs, blocks, and masks | NVIDIA | Triton vector addition |
| 38 | Fused softmax and RMSNorm | NVIDIA | Reduction kernels |
| 39 | Matrix multiplication, autotuning, and shape dispatch | NVIDIA | Multi-shape benchmark |
| 40 | Fused attention and model integration | NVIDIA | Triton integration report |
| 41 | Running Nano-vLLM and reading model layers | NVIDIA | Qwen3-0.6B eager baseline |
| 42 | Sequence, BlockManager, and Scheduler | NVIDIA | State-machine trace |
| 43 | ModelRunner, KV scatter, and attention | NVIDIA | Request call chain |
| 44 | Prefix cache, CUDA Graphs, and preemption | NVIDIA | Nano-vLLM experiment report |
| 45 | vLLM offline inference and API server | NVIDIA | Two entry-point baselines |
| 46 | EngineCore, Worker, and ModelRunner | NVIDIA | One-request architecture diagram |
| 47 | Scheduling, KV cache, concurrency, and SLOs | NVIDIA | Parameter sweep |
| 48 | Nano-vLLM and vLLM comparison | NVIDIA | Fair comparison report |
| 49 | Capstone proposal and baseline | All | Experiment design |
| 50 | Implementation, tests, and instrumentation | All | Measurable feature |
| 51 | Experiment matrix, ablations, and failure analysis | NVIDIA | Raw results and conclusions |
| 52 | Report, demo, and reproducibility review | All | Complete capstone |

## Optional topics

After the main path, choose only one topic to explore deeply: the complete Tiny-LLM Metal Week 2, tensor parallelism, speculative decoding, MoE, prefix-aware scheduling, or a vLLM contribution.

