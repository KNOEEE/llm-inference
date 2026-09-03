---
week: 3
phase: foundations
hardware: [cpu-linux, m4-mac]
estimated_hours: 8
status: planned
---

# Week 03: Modules, Parameters, and State Dictionaries

## Goals

- Understand parameter registration in nn.Module.
- Learn saving, loading, and inference mode.

## Lab

Build a module with a linear layer, buffer, and submodule, then save and restore it.

## Deliverables

- A saveable and loadable model.

## Acceptance criteria

- [ ] Produce identical output after a state-dictionary round trip.
- [ ] Explain Parameters versus buffers.

## Retrospective

- Actual time spent: 2 days
- Biggest difficulty: I didn't actually know what nn.Module was, nor what this course was about,
    and I didn't understand what linear, buffer, or submodule were. I only grasped these concepts after looking at the generated examples.
- Unresolved questions:

