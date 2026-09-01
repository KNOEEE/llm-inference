# CPU PyTorch Environment

Use this environment for PyTorch foundations, toy models, pytest, the scheduler simulator, and the load generator.

Smoke tests:

```bash
python -c 'import torch; print(torch.__version__); print(torch.ones(2, 2) @ torch.ones(2, 2))'
pytest --collect-only
```

Record the Python, PyTorch, NumPy, and pytest versions and the installation date.

