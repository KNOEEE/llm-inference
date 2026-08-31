# Tests

测试按能力分组，而不是按平台复制。

- `correctness/`：reference 与优化实现对照；
- `numerical/`：dtype、容差、极值和稳定性；
- `scheduling/`：请求状态、block/page 生命周期；
- `integration/`：端到端模型与服务。

使用根目录 `pytest.ini` 的 `cpu`、`mps`、`mlx`、`cuda` 和 `slow` marker。

