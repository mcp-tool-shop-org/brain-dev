---
title: Tools Reference
description: Complete reference for all 9 brain-dev MCP tools — analysis, generation, security, and utility.
sidebar:
  order: 2
---

brain-dev exposes 9 tools organized into four categories. Each tool is callable via the MCP protocol from any compatible client.

## Analysis tools

### coverage_analyze

Compare observed behavior patterns against test coverage to surface the gaps that matter most.

**Parameters:**
- `file_path` -- path to the source file to analyze
- `test_path` -- path to the corresponding test file (optional, auto-detected if omitted)

### behavior_missing

Find user behaviors that are not handled in code. Identifies edge cases and interaction patterns that lack coverage.

**Parameters:**
- `file_path` -- path to the source file
- `behavior_patterns` -- list of expected behavior descriptions (optional)

### refactor_suggest

Spot complexity hotspots, duplicated logic, and naming inconsistencies across your codebase.

**Parameters:**
- `file_path` -- path to the source file or directory
- `threshold` -- complexity threshold for flagging (optional, default varies by metric)

### ux_insights

Extract UX signals from usage patterns -- dropoff points, error clusters, and behavior anomalies.

**Parameters:**
- `file_path` -- path to the source file containing UX-related code
- `patterns` -- specific UX patterns to look for (optional)

## Generation tools

### tests_generate

Generate test suggestions for coverage gaps. Returns a list of test case descriptions with expected inputs and outputs.

**Parameters:**
- `file_path` -- path to the source file to generate tests for
- `coverage_report` -- existing coverage data (optional)

### smart_tests_generate

AST-based pytest generation with proper mocks, fixtures, and imports. Produces test files that compile and run.

**Parameters:**
- `file_path` -- path to the source file

**Example:**

```python
result = await client.call_tool(
    "smart_tests_generate",
    { "file_path": "/path/to/module.py" }
)
# Returns a complete pytest file with:
# - Proper imports
# - Fixtures for dependencies
# - Mock patches where needed
# - Parametrized test cases
```

### docs_generate

Find missing docstrings and generate templated documentation stubs for undocumented code.

**Parameters:**
- `file_path` -- path to the source file
- `style` -- docstring style: `google`, `numpy`, or `sphinx` (optional, defaults to `google`)

## Security tools

### security_audit

Scan for OWASP-style vulnerabilities with CWE references. Detects SQL injection, command injection, hardcoded secrets, path traversal, insecure crypto, and insecure deserialization.

**Parameters:**
- `symbols` -- list of code symbols to audit, each with `name`, `file_path`, `line`, and `source_code`
- `severity_threshold` -- minimum severity to report: `low`, `medium`, `high`, or `critical` (optional, defaults to `medium`)

**Example:**

```python
result = await client.call_tool("security_audit", {
    "symbols": [{
        "name": "execute_query",
        "file_path": "db.py",
        "line": 10,
        "source_code": "cursor.execute(f\"SELECT * FROM users WHERE id={user_id}\")"
    }],
    "severity_threshold": "medium"
})
# Returns findings with:
# - Vulnerability category
# - CWE reference
# - Severity level
# - Remediation guidance
```

See [Security Patterns](/brain-dev/handbook/security-patterns/) for the full list of vulnerability classes detected.

## Utility tools

### brain_stats

Return server statistics and configuration. Useful for verifying the server is running and checking which capabilities are available.

**Parameters:** none

## Tool summary

| Tool | Category | Description |
|------|----------|-------------|
| `coverage_analyze` | Analysis | Compare patterns to test coverage, find gaps |
| `behavior_missing` | Analysis | Find user behaviors not handled in code |
| `refactor_suggest` | Analysis | Complexity, duplication, and naming suggestions |
| `ux_insights` | Analysis | Extract UX signals from behavior patterns |
| `tests_generate` | Generation | Generate test suggestions for coverage gaps |
| `smart_tests_generate` | Generation | AST-based pytest with mocks and fixtures |
| `docs_generate` | Generation | Documentation templates for undocumented code |
| `security_audit` | Security | Scan for OWASP-style vulnerabilities |
| `brain_stats` | Utility | Server statistics and configuration |
