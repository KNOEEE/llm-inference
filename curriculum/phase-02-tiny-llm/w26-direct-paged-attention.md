---
week: 26
phase: tiny-llm
hardware: [m4-mac]
estimated_hours: 8
status: planned
---

# Week 26: Direct Paged Attention

## Goals

- Read non-contiguous KV pages directly.
- Avoid gathering pages into dense KV first.

## Lab

Compare dense, paged-gather, and direct-paged outputs.

## Deliverables

- A direct paged-attention implementation.

## Acceptance criteria

- [ ] Match all paths within tolerance.
- [ ] Confirm the hot path never rebuilds dense KV.

## Retrospective

- Actual time spent:
- Biggest difficulty:
- Unresolved questions:

