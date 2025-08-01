# Testing Guide for bamsnap

This document describes how to run tests for the bamsnap project.

## Setup

### Prerequisites
- Python 3.9+
- Poetry (for dependency management)

### Installation
```bash
# Install all dependencies including test dependencies
poetry install --with dev
```

## Running Tests

### Using Poetry (Recommended)
```bash
# Run all tests
poetry run pytest

# Run with verbose output
poetry run pytest -v

# Run with coverage report
poetry run pytest --cov=src --cov-report=html --cov-report=term

# Run only fast tests (exclude slow tests)
poetry run pytest -m "not slow"

# Run specific test categories
poetry run pytest -m "unit"        # Unit tests only
poetry run pytest -m "integration" # Integration tests only
poetry run pytest -m "cli"         # CLI tests only
```

### Using the Test Runner Script
```bash
# Make executable (first time only)
chmod +x scripts/run_tests.sh

# Run comprehensive test suite
./scripts/run_tests.sh
```

### Test Discovery
Tests are automatically discovered in the `tests/` directory following these patterns:
- Files: `test_*.py` or `*_test.py`
- Classes: `Test*`
- Functions: `test_*`

## Test Structure

```
tests/
├── __init__.py              # Test package
├── conftest.py              # Shared fixtures and configuration
├── test_examples.py         # Example tests demonstrating pytest features
├── unit/                    # Unit tests
│   ├── test_bamsnap.py      # Tests for BamSnap class
│   ├── test_util.py         # Tests for utility functions
│   └── test_cli.py          # Tests for CLI functionality
├── integration/             # Integration tests
│   └── test_workflows.py    # End-to-end workflow tests
└── fixtures/                # Test data and fixtures
```

## Test Categories and Markers

Tests are organized using pytest markers:

- `@pytest.mark.unit` - Fast, isolated unit tests
- `@pytest.mark.integration` - Integration tests that may be slower
- `@pytest.mark.slow` - Tests that take significant time
- `@pytest.mark.cli` - Command-line interface tests

### Running Specific Test Types
```bash
# Run only unit tests
poetry run pytest -m "unit"

# Run everything except slow tests
poetry run pytest -m "not slow"

# Run integration tests
poetry run pytest -m "integration"
```

## Available Fixtures

Common fixtures are defined in `tests/conftest.py`:

- `temp_dir` - Temporary directory for test files
- `sample_bam_file` - Creates a sample BAM file for testing
- `sample_bam_index` - Creates a corresponding BAM index file
- `sample_bamlist_file` - Creates a sample bamlist file
- `mock_logger` - Mock logger for testing
- `mock_options` - Mock options dictionary
- `sample_positions` - Sample genomic positions
- `mock_bam_object` - Mock BAM object

### Using Fixtures in Tests
```python
def test_my_function(temp_dir, mock_logger):
    # temp_dir is a pathlib.Path to a temporary directory
    test_file = temp_dir / "test.txt"
    test_file.write_text("content")
    
    # mock_logger can be used to verify logging calls
    mock_logger.info.assert_called_with("expected message")
```

## Writing New Tests

### Unit Test Example
```python
import pytest
from src.util import file_exist

class TestFileOperations:
    def test_file_exist_with_real_file(self, temp_dir):
        test_file = temp_dir / "test.txt"
        test_file.write_text("content")
        
        assert file_exist(str(test_file)) is True

    @pytest.mark.parametrize("input,expected", [
        ("chr1", True),
        ("1", True),
        ("invalid", False),
    ])
    def test_chromosome_validation(self, input, expected):
        result = input.startswith('chr') or input.isdigit()
        assert result == expected
```

### Integration Test Example
```python
@pytest.mark.integration
def test_complete_workflow(self, sample_bam_file, sample_bam_index):
    # Test that involves multiple components
    pass
```

## Coverage Reports

After running tests with coverage, you can view reports:

- **Terminal**: Coverage summary printed to terminal
- **HTML**: Open `htmlcov/index.html` in your browser for detailed report

```bash
# Generate and view HTML coverage report
poetry run pytest --cov=src --cov-report=html
open htmlcov/index.html
```

## Continuous Integration

Tests are automatically run on GitHub Actions for:
- Python versions: 3.9, 3.10, 3.11, 3.12
- On push to main/develop branches
- On pull requests

See `.github/workflows/tests.yml` for CI configuration.

## Common Issues

### Import Errors
If you see import errors when running tests:
```bash
# Make sure the package is installed in development mode
poetry install

# Check that src/ is in the Python path (conftest.py handles this)
```

### Coverage Warnings
"No data was collected" warnings are normal when testing logic that doesn't import your source code.

### Slow Tests
Use the `@pytest.mark.slow` decorator for tests that take a long time:
```python
@pytest.mark.slow
def test_expensive_operation():
    # This test will be skipped when running with -m "not slow"
    pass
```

## Configuration

Test configuration is in `pyproject.toml` under `[tool.pytest.ini_options]`:

- Test discovery paths
- Coverage settings
- Default command line options
- Marker definitions

## Best Practices

1. **Keep tests fast**: Unit tests should run in milliseconds
2. **Use fixtures**: Share common setup code via fixtures
3. **Mark slow tests**: Use `@pytest.mark.slow` for tests > 1 second
4. **Test edge cases**: Include empty inputs, invalid data, etc.
5. **Use descriptive names**: Test function names should describe what they test
6. **One assertion per test**: Keep tests focused and simple
7. **Mock external dependencies**: Use mocks for file I/O, network calls, etc.

## Adding New Test Dependencies

```bash
# Add a new test dependency
poetry add --group dev pytest-asyncio

# Update lock file
poetry lock

# Install updated dependencies
poetry install --with dev
```
