"""
Dev Brain - Intelligent developer insights MCP server.

Consumes Context Engine to provide:
- Test coverage analysis
- Behavior gap detection
- Test generation suggestions
- Refactoring recommendations
- UX insights

Usage:
    # As MCP server
    brain-dev

    # Programmatic
    from brain_dev import DevBrainConfig
    from brain_dev.server import create_server
"""

from importlib.metadata import version, PackageNotFoundError

from .config import DevBrainConfig

try:
    __version__: str = version("brain-dev")
except PackageNotFoundError:
    __version__ = "0.0.0"  # editable / not installed

__all__ = [
    "DevBrainConfig",
    "__version__",
]
