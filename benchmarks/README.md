# Benchmark Protocol

Performance results must be both correct and reproducible.

## Required metadata

- repository commit, dependency versions, device, and driver;
- model, weight format, dtype, and sampling parameters;
- prompt/output length and batch size/concurrency;
- warmup procedure, synchronization method, and sample count;
- TTFT, TPOT, throughput, p50/p95, memory usage, and error rate.

## Constraints

- Do not require token-by-token bit equality across different weight formats.
- Do not include first-time compilation in steady-state kernel latency.
- Do not use absolute Mac-versus-NVIDIA throughput to rank backends.
- Raw results must follow `schemas/result.schema.json`; large files belong under `artifacts/`.

