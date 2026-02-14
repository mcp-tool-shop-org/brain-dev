"""Verify that the runtime version matches pyproject.toml."""

from __future__ import annotations

import re
from pathlib import Path

import brain_dev


_PYPROJECT = Path(__file__).resolve().parents[1] / "pyproject.toml"


def _read_pyproject_version() -> str:
    """Extract version = "x.y.z" from pyproject.toml."""
    text = _PYPROJECT.read_text(encoding="utf-8")
    match = re.search(r'^version\s*=\s*"([^"]+)"', text, re.MULTILINE)
    assert match, "could not find version in pyproject.toml"
    return match.group(1)


def test_version_is_set():
    """__version__ must be a non-empty string."""
    assert isinstance(brain_dev.__version__, str)
    assert brain_dev.__version__  # not empty


def test_version_matches_pyproject():
    """Runtime __version__ must match pyproject.toml version."""
    pyproject_version = _read_pyproject_version()
    assert brain_dev.__version__ == pyproject_version, (
        f"brain_dev.__version__ ({brain_dev.__version__!r}) "
        f"!= pyproject.toml ({pyproject_version!r}). "
        "Did you forget to reinstall after bumping the version?"
    )
