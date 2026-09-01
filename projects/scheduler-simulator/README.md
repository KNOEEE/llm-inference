# Scheduler Simulator

Use CPU execution and scripted models to test request states, token budgets, continuous batching, chunked prefill, block allocation, page reuse, and preemption.

Determinism is the key property: for a fixed request sequence and page pool, tests should assert the waiting/running queues and block table at every step.

