<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.md">English</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/brain-dev/readme.png" width="400" alt="brain-dev" />
</p>

<p align="center">
  <a href="https://github.com/mcp-tool-shop-org/brain-dev/actions/workflows/test.yml"><img src="https://github.com/mcp-tool-shop-org/brain-dev/actions/workflows/test.yml/badge.svg" alt="Tests" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" /></a>
  <a href="https://mcp-tool-shop-org.github.io/brain-dev/"><img src="https://img.shields.io/badge/Landing_Page-live-blue" alt="Landing Page" /></a>
  <a href="https://pypi.org/project/dev-brain/"><img src="https://img.shields.io/pypi/v/dev-brain" alt="PyPI" /></a>
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.11+-blue.svg" alt="Python 3.11+" /></a>
</p>

**用于开发者洞察的智能层**——通过 MCP 提供代码覆盖率分析、测试生成、重构建议、安全审计以及用户体验洞察。

## 功能

- **9 个分析工具**——代码覆盖率缺口、行为分析、测试生成、重构、用户体验洞察、安全审计等。
- **基于 AST 的测试生成**——自动生成带有实际可编译的模拟对象的 pytest 测试。
- **安全漏洞检测**——采用 OWASP 风格的扫描，检测 SQL 注入、命令注入以及硬编码的敏感信息。
- **文档分析**——查找缺失的文档字符串，并提供模板建议。
- **原生支持 MCP**——与 Claude 以及其他 MCP 客户端无缝集成。

## 安装

```bash
pip install dev-brain
```

或用于开发：

```bash
git clone https://github.com/mcp-tool-shop-org/brain-dev.git
cd brain-dev
pip install -e ".[dev]"
```

## 快速开始

```bash
# Run the MCP server
dev-brain
```

添加到 Claude 桌面配置 (`claude_desktop_config.json`)：

```json
{
  "mcpServers": {
    "dev-brain": {
      "command": "dev-brain"
    }
  }
}
```

## 工具

### 分析工具

| 工具 | 描述 |
| ------ | ------------- |
| `coverage_analyze` | 将观察到的模式与测试覆盖率进行比较，查找缺口。 |
| `behavior_missing` | 查找代码中未处理的用户行为。 |
| `refactor_suggest` | 根据复杂性、重复性和命名建议进行重构。 |
| `ux_insights` | 从用户行为模式（例如，流失率、错误）中提取用户体验洞察。 |

### 生成工具

| 工具 | 描述 |
| ------ | ------------- |
| `tests_generate` | 为代码覆盖率缺口生成测试建议。 |
| `smart_tests_generate` | 基于 AST 的 pytest 生成，包含正确的模拟对象和测试用例。 |
| `docs_generate` | 为未 documented 的代码生成文档模板。 |

### 安全工具

| 工具 | 描述 |
| ------ | ------------- |
| `security_audit` | 扫描潜在的安全漏洞（例如，SQL 注入、命令注入、敏感信息等）。 |

### 实用工具

| 工具 | 描述 |
| ------ | ------------- |
| `brain_stats` | 获取服务器统计信息和配置。 |

## 示例用法

### 安全审计

```python
# Via MCP client
result = await client.call_tool("security_audit", {
    "symbols": [
        {
            "name": "execute_query",
            "file_path": "db.py",
            "line": 10,
            "source_code": "cursor.execute(f\"SELECT * FROM users WHERE id = {user_id}\")"
        }
    ],
    "severity_threshold": "medium"
})
# Returns: SQL injection vulnerability detected (CWE-89)
```

### 智能测试生成

```python
result = await client.call_tool("smart_tests_generate", {
    "file_path": "/path/to/your/module.py"
})
# Returns complete pytest file with fixtures and mocks
```

## 架构

```
┌─────────────────────────────────────────────────────────────┐
│                      DEV BRAIN MCP SERVER                    │
├─────────────────────────────────────────────────────────────┤
│  Analyzers                                                   │
│  ├─ CoverageAnalyzer    (test gaps)                         │
│  ├─ BehaviorAnalyzer    (unhandled flows)                   │
│  ├─ RefactorAnalyzer    (complexity, naming)                │
│  ├─ UXAnalyzer          (dropoff, errors)                   │
│  ├─ DocsAnalyzer        (missing docs)                      │
│  └─ SecurityAnalyzer    (vulnerabilities)                   │
├─────────────────────────────────────────────────────────────┤
│  Generators                                                  │
│  ├─ TestGenerator       (skeleton tests)                    │
│  └─ SmartTestGenerator  (AST-based pytest)                  │
└─────────────────────────────────────────────────────────────┘
```

## 检测到的安全模式

| 类别 | 严重程度 | CWE |
| ---------- | ---------- | ----- |
| SQL 注入 | 严重 | CWE-89 |
| 命令注入 | 严重 | CWE-78 |
| 不安全的序列化 | 严重 | CWE-502 |
| 硬编码的敏感信息 | 高 | CWE-798 |
| 路径遍历 | 高 | CWE-22 |
| 不安全的加密 | 中等 | CWE-327 |

## 开发

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=dev_brain --cov-report=html

# Type checking (optional)
mypy dev_brain
```

## 许可证

MIT 许可证——详情请参见 [LICENSE](LICENSE)。

---

由 <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a> 构建。
