from __future__ import annotations
import importlib
import sys
from types import ModuleType

__version__ = "0.0.1"
__author__ = "krab/pena"
__license__ = "MIT"
__description__ = "Reporting framework: Python interface for C core"

_core: ModuleType | None = None

def _load_core() -> ModuleType | None:
    names = ("reports_core", "_reports", "reports_c.core")
    for name in names:
        try:
            mod = importlib.import_module(name)
            return mod
        except ModuleNotFoundError:
            continue
    return None


_core = _load_core()


def is_core_loaded() -> bool:
    return _core is not None


def version() -> str:
    cver = getattr(_core, "version", None)
    cver_str = f"C-core: {cver()}" if callable(cver) else "C-core: not loaded"
    return f"Reports {__version__} ({cver_str})"


def echo(msg: str) -> str:
    if _core and hasattr(_core, "echo"):
        return _core.echo(msg)
    return f"reports (python): {msg}"



__all__ = [
    "__version__",
    "version",
    "is_core_loaded",
    "echo",
]
