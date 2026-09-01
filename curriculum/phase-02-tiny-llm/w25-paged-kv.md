---
week: 25
phase: tiny-llm
hardware: [m4-mac]
estimated_hours: 8
status: planned
---

# Week 25: Paged KV Allocator

## Goals

- Understand logical blocks and physical pages.
- Implement allocation, release, and reuse invariants.

## Lab

Shrink the page pool under a scripted model to force boundaries.

## Deliverables

- BlockManager state-machine tests.

## Acceptance criteria

- [ ] Prevent leaks and double frees.
- [ ] Predict the block table at every step.

## Retrospective

- Actual time spent:
- Biggest difficulty:
- Unresolved questions:

