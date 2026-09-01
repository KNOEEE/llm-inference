# LLM Inference Course

A 52-week hands-on curriculum for learners who are new to LLM inference systems. The main path starts with PyTorch tensors and Transformer forward passes, then moves through Tiny-LLM, MLX/Metal, CUDA, Triton, Nano-vLLM, and vLLM before ending with a reproducible inference project.

## Learning outcomes

After completing the main path, you should be able to:

- implement and validate a small decoder-only Transformer independently;
- explain prefill, decode, KV cache, continuous batching, chunked prefill, and paged KV;
- build a PyTorch oracle for an operator and implement at least one optimized Metal, CUDA, or Triton version;
- trace one request through scheduling, KV management, and model execution in Nano-vLLM and vLLM;
- evaluate an inference system with TTFT, TPOT, throughput, memory usage, and tail latency;
- deliver a reproducible experiment with environment metadata, tests, raw results, and a failure retrospective.

## Hardware roles

| Environment | Primary responsibilities | Out of scope |
|---|---|---|
| M4 MacBook | PyTorch/MPS, MLX, Tiny-LLM, and selected Metal kernels | CUDA and canonical Nano-vLLM/vLLM performance conclusions |
| CPU Linux | Unit tests, toy models, scheduler simulation, APIs, load generation, and code reading | GPU kernel performance conclusions |
| NVIDIA Linux | CUDA, Triton, FlashAttention, Nano-vLLM, vLLM, and real performance experiments | Do not substitute CPU results when a GPU is unavailable |

## How to use this repository

1. Read [ROADMAP.md](ROADMAP.md) to identify the current phase and weekly topic.
2. Open the matching weekly page under `curriculum/`.
3. Put small, disposable exercises under `labs/`.
4. Put implementations that evolve across multiple weeks under `projects/`.
5. Use the fixed workloads and result format under `benchmarks/` for every performance claim.
6. Complete the matching phase report under `reports/` at the end of each phase.

The suggested pace is about eight hours per week: two hours of reading, four to five hours of coding, one to two hours of testing and benchmarking, and the remaining time for notes. Progress by acceptance criteria rather than calendar deadlines.

## Repository structure

```text
curriculum/    The 52-week curriculum and weekly acceptance criteria
labs/          Small exercises that may be discarded or repeated
projects/      Long-lived projects that evolve across phases
benchmarks/    Workloads, result schema, and experiment reports
tests/         Cross-project testing conventions
environments/  Independent environment notes for each platform
upstreams/     External repository URLs, paths, and commit records
notes/         Concepts, papers, debugging notes, and retrospectives
reports/       Phase summaries
scripts/       Environment and curriculum validation tools
artifacts/     Models, profiles, and other large untracked files
```

## Three progression rules

- Do not start kernel optimization until you can derive tensor shapes independently.
- Do not claim a speedup without a correctness oracle and synchronized benchmark.
- Do not dive into the vLLM repository until you can draw the scheduler, block table, and KV page lifecycle.

## Progress

- [ ] Phase 1: PyTorch and Transformer foundations (W01-W10)
- [ ] Phase 2: Tiny-LLM and serving fundamentals (W11-W28)
- [ ] Phase 3: Engineering and measurement (W29-W32)
- [ ] Phase 4: CUDA (W33-W36)
- [ ] Phase 5: Triton (W37-W40)
- [ ] Phase 6: Nano-vLLM (W41-W44)
- [ ] Phase 7: vLLM (W45-W48)
- [ ] Phase 8: Capstone (W49-W52)
