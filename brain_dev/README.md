# Brain-Dev: Intelligent Developer Insights MCP Server

A powerful Model Context Protocol (MCP) server that provides intelligent developer insights through comprehensive code analysis. Brain-Dev consumes context data to deliver:

- 🧪 **Test Coverage Analysis** - Identify gaps in your test suite
- 🔍 **Behavior Gap Detection** - Find unhandled user behaviors
- ✨ **Smart Test Generation** - Auto-generate test suggestions with AST-based analysis
- 🔧 **Refactoring Recommendations** - Get suggestions for code improvements
- 📊 **UX Insights** - Extract patterns from user behavior data
- 🔐 **Security Analysis** - Identify potential security concerns
- 📚 **Documentation Analysis** - Check documentation completeness

## Features

### Coverage Gap Analysis
Analyzes your codebase against observed usage patterns to identify what's not being tested:

```python
analyzer = CoverageAnalyzer(min_support=0.05)
gaps = analyzer.analyze_gaps(observed_patterns, existing_tests)
# Returns prioritized coverage gaps with suggested test names
```

### Smart Test Generation
Uses AST-based code analysis to generate complete, working test cases:

```python
from brain_dev.smart_test_generator import generate_tests_for_file

test_code = generate_tests_for_file("path/to/module.py")
# Returns full pytest test file with fixtures and mocks
```

### Behavior Analysis
Discovers user behaviors captured in telemetry that aren't handled in code:

```python
analyzer = BehaviorAnalyzer()
missing = analyzer.find_missing_behaviors(patterns, code_symbols)
# Returns behaviors to implement
```

### Refactoring Suggestions
Identifies opportunities for code improvements:

- Extract functions for complex logic
- Rename variables for clarity
- Simplify deeply nested code
- Fix security anti-patterns

## Installation

### From Source
```bash
cd brain_dev
pip install -e ".[dev]"
```

### As MCP Server
```bash
pip install brain-dev
brain-dev  # Starts the MCP server on stdio
```

## Configuration

Configure via `DevBrainConfig`:

```python
from brain_dev import DevBrainConfig
from brain_dev.server import create_server

config = DevBrainConfig(
    min_gap_support=0.05,      # Minimum support threshold
    min_confidence=0.5,         # Minimum confidence for suggestions
    max_suggestions=20,         # Max suggestions per request
    default_test_framework="pytest",
    complexity_threshold=10,    # Cyclomatic complexity limit
)

server = create_server(config)
```

## Usage as MCP Server

Brain-Dev implements the Model Context Protocol and provides these tools:

### Tools

1. **coverage_analyze** - Analyze test coverage gaps
   - Input: observed patterns, existing tests
   - Output: prioritized coverage gaps with test suggestions

2. **behavior_missing** - Find unhandled user behaviors  
   - Input: observed patterns, code symbols
   - Output: missing behaviors with implementation suggestions

3. **tests_generate** - Generate test suggestions
   - Input: coverage gap
   - Output: ready-to-use test code

4. **refactor_suggest** - Suggest refactoring opportunities
   - Input: code analysis data
   - Output: refactoring suggestions with confidence scores

5. **ux_insights** - Extract UX insights from behavior
   - Input: behavior patterns
   - Output: user experience findings and recommendations

## Testing

Run the test suite:

```bash
# All tests
pytest

# With coverage
pytest --cov=brain_dev

# Specific test file
pytest tests/test_smart_generator.py -v

# Only integration tests
pytest -m integration
```

Test files:
- `test_analyzer.py` - Core analyzer tests
- `test_smart_generator.py` - Test generation tests
- `test_server.py` - MCP server tests
- `test_integration.py` - End-to-end integration tests
- `test_coverage_gaps.py` - Coverage analysis tests
- `test_new_analyzers.py` - New analyzer tests
- `test_new_tools.py` - New tool tests

## Architecture

### Core Components

**analyzer.py** - Analysis engine with dataclasses for:
- `CoverageGap` - Represents a gap in test coverage
- `MissingBehavior` - User behavior not in code
- `SuggestedUnitCase` - Generated test suggestion
- `RefactorSuggestion` - Code improvement recommendation
- `UXInsight` - User experience finding

Analyzer classes:
- `CoverageAnalyzer` - Identifies test coverage gaps
- `BehaviorAnalyzer` - Finds unhandled behaviors
- `TestGenerator` - Generates test code
- `RefactorAnalyzer` - Suggests refactoring
- `UXAnalyzer` - Analyzes user experience
- `DocsAnalyzer` - Checks documentation
- `SecurityAnalyzer` - Identifies security issues

**smart_test_generator.py** - AST-based test generation
- `CodeAnalyzer` - Parses code with AST
- `MockDetector` - Identifies mock requirements
- `SmartPytestFileGenerator` - Generates pytest files

**server.py** - MCP server implementation
- `create_server()` - Factory function for MCP server
- Lazy-loaded analyzer instances
- Tool handlers for each analysis type

**config.py** - Configuration management
- `DevBrainConfig` - Dataclass with analysis thresholds
- `load_config()` - Load from environment/file

### Data Flow

```
Context Data (patterns, code symbols)
         ↓
    Analyzers (Core analysis logic)
         ↓
    Data Models (Gap, Behavior, etc.)
         ↓
    MCP Server (Protocol implementation)
         ↓
    Client Tools (Claude, other LLMs)
```

## Best Practices (2026)

- Uses `ast.NodeVisitor` for accurate Python parsing
- Async-ready with pytest-asyncio support
- Type hints throughout for better IDE support
- Comprehensive docstrings and examples
- Lazy initialization pattern for analyzers
- Configuration-driven behavior

## Development

### Code Quality

```bash
# Format code
black brain_dev tests

# Sort imports
isort brain_dev tests

# Lint
ruff check brain_dev tests

# Type check
mypy brain_dev

# All checks
pytest --cov=brain_dev && black --check brain_dev && mypy brain_dev
```

### Adding New Analyzers

1. Create analyzer class inheriting from base pattern
2. Implement analysis method returning typed result
3. Add to server.py with lazy getter
4. Write tests in tests/
5. Add tool handler in server.py

### Adding Tests

```python
from brain_dev.analyzer import CoverageGap

def test_coverage_analysis():
    analyzer = CoverageAnalyzer()
    gaps = analyzer.analyze_gaps(patterns, tests)
    assert len(gaps) > 0
    assert gaps[0].priority in ["low", "medium", "high", "critical"]
```

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

## License

MIT - See [LICENSE](../LICENSE)

## Related Projects

- **Context Engine** - Provides pattern and code analysis data
- **MCP** - Model Context Protocol specification
- **Aspire AI** - Integration with AI systems

## Support

For issues, questions, or contributions, please open an issue or submit a PR.

---

**Version:** 1.0.0  
**Status:** Active Development  
**Last Updated:** January 2026
