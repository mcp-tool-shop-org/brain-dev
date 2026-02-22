# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] — 2026-02-22

### Added

- **9 Analysis Tools** for comprehensive developer insights:
  - Coverage gap detection and analysis
  - Behavior analysis for functions and modules
  - Automated pytest test generation with mocks
  - Refactoring suggestions and recommendations
  - Security vulnerability scanning (OWASP-style)
  - Documentation analysis and missing docstring detection
  - UX insights and interaction analysis
  - Complexity metrics and performance analysis
  - Code quality scoring

- **AST-Based Test Generation** — Automatically generate pytest tests with proper mocks that compile and run
- **Security Vulnerability Detection** — Detect SQL injection, command injection, hardcoded secrets, and other OWASP vulnerabilities
- **MCP Integration** — Native Model Context Protocol support for Claude and other MCP clients
- **Python 3.11+** support

### Infrastructure

- GitHub Actions CI/CD with pytest coverage tracking
- Type checking with mypy
- Linting with ruff

## [Unreleased]

_No unreleased changes._
