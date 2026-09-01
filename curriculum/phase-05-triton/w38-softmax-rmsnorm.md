---
week: 38
phase: triton
hardware: [nvidia-linux]
estimated_hours: 8
status: planned
---

# Week 38: Fused Softmax and RMSNorm

## Goals

- Learn reductions and numerical stability.
- Recreate the cross-backend RMSNorm comparison.

## Lab

Implement fused softmax and inference-only RMSNorm.

## Deliverables

- Two Triton reduction kernels.

## Acceptance criteria

- [ ] Match the PyTorch oracle.
- [ ] Test irregular sizes and large values.

## Retrospective

- Actual time spent:
- Biggest difficulty:
- Unresolved questions:

