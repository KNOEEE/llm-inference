# CPU PyTorch Environment

用于 PyTorch 基础、toy model、pytest、scheduler simulator 和 load generator。

Smoke test：

```bash
python -c 'import torch; print(torch.__version__); print(torch.ones(2, 2) @ torch.ones(2, 2))'
pytest --collect-only
```

记录 Python、PyTorch、NumPy、pytest 版本和安装日期。

