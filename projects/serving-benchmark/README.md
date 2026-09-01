# Serving Benchmark

Provide a consistent workload and metric definition for Tiny-LLM, Nano-vLLM, and vLLM.

At minimum, support:

- fixed prompt and output lengths;
- mixed short and long requests;
- concurrency sweeps;
- shared-prefix ratios;
- TTFT, TPOT, request/token throughput, p50/p95, and error rate.

