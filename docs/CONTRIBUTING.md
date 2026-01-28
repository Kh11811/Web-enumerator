# Contributing to Web-enumerator

Thank you for your interest in contributing to Web-enumerator! This document provides guidelines for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)
- [Code Style Guidelines](#code-style-guidelines)
- [Submitting Pull Requests](#submitting-pull-requests)
- [Testing Guidelines](#testing-guidelines)

---

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment. We expect all contributors to:

- Be respectful and constructive in communication
- Welcome newcomers and help them get started
- Focus on what is best for the community
- Show empathy towards other community members

---

## How to Contribute

There are many ways to contribute to Web-enumerator:

1. **Report bugs** - Help us identify issues
2. **Suggest features** - Share ideas for improvements
3. **Write documentation** - Improve or expand docs
4. **Submit code** - Fix bugs or implement features
5. **Review pull requests** - Provide feedback on contributions
6. **Share the project** - Help others discover it

---

## Reporting Bugs

Before creating a bug report, please check existing issues to avoid duplicates.

### How to Submit a Bug Report

1. **Use a clear and descriptive title**
2. **Describe the exact steps to reproduce the problem**
3. **Provide specific examples** (commands, wordlists, URLs)
4. **Describe the behavior you observed** and what you expected
5. **Include system information**:
   - OS and version
   - Python version (for Python script)
   - Bash version (for Bash script)
   - Version of Web-enumerator

### Bug Report Template

```markdown
## Description
A clear description of the bug.

## Steps to Reproduce
1. Run command: `bash src/enumerator.sh ...`
2. Using wordlist: `examples/sample_wordlist.txt`
3. Target URL: `https://example.com`

## Expected Behavior
What you expected to happen.

## Actual Behavior
What actually happened.

## System Information
- OS: Ubuntu 22.04
- Python: 3.10.6
- Bash: 5.1.16

## Additional Context
Any other relevant information.
```

---

## Suggesting Features

We welcome feature suggestions! Before submitting:

1. **Check existing issues** for similar suggestions
2. **Consider if it aligns** with project goals (educational, simple, lightweight)
3. **Provide a clear use case** for the feature

### Feature Request Template

```markdown
## Feature Description
A clear description of the feature.

## Use Case
Why this feature would be useful.

## Proposed Implementation
(Optional) How you think it could be implemented.

## Alternatives Considered
Other approaches you've considered.
```

---

## Code Style Guidelines

### General Principles

- **Keep it simple** - This is an educational tool
- **Maintain readability** - Code should be easy to understand
- **Follow existing patterns** - Match the style of existing code
- **Add comments** for complex logic

### Bash Script Guidelines

- Use consistent indentation (tabs or spaces, match existing)
- Add comments for non-obvious commands
- Use meaningful variable names
- Handle errors appropriately
- Follow shell scripting best practices

```bash
# Good example
if [ $# -ne 2 ]; then
    echo "Error: missing arguments" >&2
    exit 1
fi

# Check if file exists
if [ ! -f "$1" ]; then
    echo "Error: wordlist file not found" >&2
    exit 1
fi
```

### Python Script Guidelines

- Follow [PEP 8](https://pep8.org/) style guide
- Use 4 spaces for indentation
- Add docstrings for functions
- Use meaningful variable names
- Handle exceptions appropriately
- Type hints are welcome but not required

```python
# Good example
def enumerate_paths(wordlist_path: str, base_url: str) -> list:
    """
    Enumerate web paths using a wordlist.
    
    Args:
        wordlist_path: Path to the wordlist file
        base_url: Base URL to enumerate
        
    Returns:
        List of successful paths
    """
    results = []
    # Implementation
    return results
```

---

## Submitting Pull Requests

### Before Submitting

1. **Fork the repository** and create a branch for your changes
2. **Test your changes** thoroughly
3. **Update documentation** if needed
4. **Follow code style guidelines**
5. **Write clear commit messages**

### Pull Request Process

1. **Create a descriptive title**
   - Good: "Fix shebang line in enumerator.sh"
   - Bad: "Fix bug"

2. **Provide detailed description**
   - What changes were made
   - Why the changes were necessary
   - How to test the changes

3. **Reference related issues** if applicable
   - "Fixes #123"
   - "Relates to #456"

4. **Keep PRs focused**
   - One feature or fix per PR
   - Avoid mixing unrelated changes

5. **Be responsive to feedback**
   - Address review comments
   - Update PR as needed

### PR Template

```markdown
## Description
Brief description of changes.

## Motivation
Why these changes are needed.

## Changes Made
- Changed X to Y
- Added feature Z
- Fixed bug in W

## Testing
How the changes were tested.

## Checklist
- [ ] Code follows style guidelines
- [ ] Tests pass
- [ ] Documentation updated
- [ ] No new warnings
```

---

## Testing Guidelines

### Running Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run Python tests
python -m pytest tests/

# Run bash script tests (if available)
bash tests/test_bash_script.sh
```

### Writing Tests

When adding new features, please include tests:

1. **Unit tests** for individual functions
2. **Integration tests** for complete workflows
3. **Edge case tests** for error handling

### Test Structure

```python
import pytest
from unittest.mock import Mock, patch

def test_valid_input():
    """Test with valid input."""
    # Arrange
    # Act
    # Assert
    pass

def test_invalid_input():
    """Test error handling with invalid input."""
    # Test edge cases
    pass

def test_http_responses():
    """Test different HTTP response codes."""
    # Mock HTTP responses
    pass
```

---

## Development Setup

### Prerequisites

- Git
- Python 3.7+
- Bash shell
- curl (for Bash script)

### Setup Steps

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/Web-enumerator.git
cd Web-enumerator

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/
```

---

## Questions?

If you have questions about contributing:

1. Check existing documentation
2. Search existing issues
3. Open a new issue with your question

---

## License

By contributing to Web-enumerator, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Web-enumerator! 🎉
