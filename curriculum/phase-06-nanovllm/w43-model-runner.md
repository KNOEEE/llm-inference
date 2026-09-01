---
week: 43
phase: nanovllm
hardware: [nvidia-linux]
estimated_hours: 8
status: planned
---

# Week 43: ModelRunner, KV Scatter, and Attention

## Goals

- Trace batch metadata into kernels.
- Distinguish prefill and decode attention.

## Lab

Follow one request through slots, KV storage, attention, and sampling.

## Deliverables

- A complete request call chain.

## Acceptance criteria

- [ ] Identify PyTorch, Triton, and FlashAttention roles.
- [ ] Link sequences to physical slots.

## Retrospective

- Actual time spent:
- Biggest difficulty:
- Unresolved questions:

