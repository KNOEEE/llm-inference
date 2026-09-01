---
week: 17
phase: tiny-llm
hardware: [m4-mac]
estimated_hours: 8
status: planned
---

# Week 17: Dense KV Cache

## Goals

- Make every layer cache request-owned.
- Handle positions and appends correctly.

## Lab

Compare cache-on and cache-off results across prompt and output lengths.

## Deliverables

- A dense KV-cache implementation.

## Acceptance criteria

- [ ] Produce identical greedy output.
- [ ] Stop recomputing old K/V during decode.

## Retrospective

- Actual time spent:
- Biggest difficulty:
- Unresolved questions:

