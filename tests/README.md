# Tests

Organize tests by capability rather than duplicating them by platform.

- `correctness/`: compare reference and optimized implementations;
- `numerical/`: dtypes, tolerances, extreme values, and stability;
- `scheduling/`: request states and block/page lifecycles;
- `integration/`: end-to-end models and services.

Use the `cpu`, `mps`, `mlx`, `cuda`, and `slow` markers defined in the root `pytest.ini`.

