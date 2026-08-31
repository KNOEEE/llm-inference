#!/usr/bin/env python3
"""Print reproducibility metadata as JSON; never reads secrets."""

from __future__ import annotations

import json
import platform
from pathlib import Path
import shutil
import subprocess
import sys
from typing import Any

try:
    from importlib import metadata as importlib_metadata
except ImportError:  # Python 3.7
    importlib_metadata = None


ROOT = Path(__file__).resolve().parents[1]


def run(command: list[str]) -> str | None:
    try:
        result = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            timeout=5,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    output = (result.stdout or result.stderr).strip()
    return output or None


def version(package: str) -> str | None:
    if importlib_metadata is not None:
        try:
            return importlib_metadata.version(package)
        except importlib_metadata.PackageNotFoundError:
            return None

    module_name = {"mlx-lm": "mlx_lm"}.get(package, package)
    try:
        module = __import__(module_name)
    except ImportError:
        return None
    return getattr(module, "__version__", "installed")


def torch_info() -> dict[str, Any] | None:
    try:
        import torch
    except ImportError:
        return None

    info: dict[str, Any] = {
        "version": torch.__version__,
        "cuda_available": torch.cuda.is_available(),
        "mps_available": bool(
            hasattr(torch.backends, "mps") and torch.backends.mps.is_available()
        ),
    }
    if torch.cuda.is_available():
        info["cuda_version"] = torch.version.cuda
        info["device_name"] = torch.cuda.get_device_name(0)
        info["device_capability"] = torch.cuda.get_device_capability(0)
    return info


def main() -> None:
    data = {
        "platform": platform.platform(),
        "machine": platform.machine(),
        "python": sys.version.split()[0],
        "git_commit": run(["git", "-C", str(ROOT), "rev-parse", "HEAD"]),
        "tools": {
            "git": run(["git", "--version"]),
            "nvcc": run(["nvcc", "--version"]) if shutil.which("nvcc") else None,
            "nvidia_smi": run([
                "nvidia-smi",
                "--query-gpu=name,driver_version,memory.total",
                "--format=csv,noheader",
            ]) if shutil.which("nvidia-smi") else None,
        },
        "packages": {
            name: version(name)
            for name in ("numpy", "pytest", "torch", "mlx", "mlx-lm", "triton")
        },
        "torch": torch_info(),
    }
    print(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
