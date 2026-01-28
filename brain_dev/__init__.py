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

from .config import DevBrainConfig

__version__ = "1.0.0"
__all__ = [
    "DevBrainConfig",
]
