# Contributing to FillMyBlank.AI

Thank you for your interest in contributing to FillMyBlank.AI! We welcome contributions from everyone.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- VSCode (recommended)

### Development Setup

1. Fork the repository
2. Clone your fork:
```bash
git clone https://github.com/yourusername/fillmyblank-ai.git
cd fillmyblank-ai
```

3. Install dependencies:
```bash
pip install -r requirements.txt
pip install -e ".[dev]"  # Install development dependencies
```

4. Set up pre-commit hooks (optional but recommended):
```bash
pre-commit install
```

## 🛠️ Development Workflow

### Code Style

We use the following tools to maintain code quality:

- **Ruff**: For linting and import sorting
- **Black**: For code formatting
- **pytest**: For testing

Run these commands before committing:

```bash
# Format code
black .

# Lint code
ruff check .

# Run tests
pytest
```

### VSCode Integration

This project includes VSCode configuration files that will:
- Automatically format code on save
- Run linting in real-time
- Provide debug configurations
- Suggest recommended extensions

## 📝 Making Changes

### Branch Naming

Use descriptive branch names:
- `feature/add-new-game-type`
- `bugfix/fix-audio-playback`
- `docs/update-readme`

### Commit Messages

Follow conventional commit format:
- `feat: add new matching game`
- `fix: resolve audio playback issue`
- `docs: update installation instructions`
- `refactor: reorganize game modules`

### Pull Request Process

1. Create a feature branch from `main`
2. Make your changes
3. Add/update tests as needed
4. Update documentation if necessary
5. Ensure all tests pass
6. Create a pull request using our [MR template](.gitlab/merge_request_templates/Default.md)

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=.

# Run specific test file
pytest tests/test_games.py
```

### Writing Tests

- Place tests in the `tests/` directory
- Name test files with `test_` prefix
- Use descriptive test function names
- Include both positive and negative test cases

## 🐛 Reporting Issues

### Bug Reports

Use our [bug report template](.gitlab/issue_templates/Bug.md) and include:
- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Environment details
- Screenshots if applicable

### Feature Requests

Use our [feature request template](.gitlab/issue_templates/Feature_Request.md) and include:
- Clear description of the feature
- Use case and motivation
- Proposed implementation (if any)

## 📚 Documentation

### Code Documentation

- Use docstrings for all functions and classes
- Follow Google-style docstring format
- Include type hints where appropriate

### README Updates

When adding new features or making significant changes:
- Update the README.md
- Add examples if applicable
- Update the project structure section

## 🎯 Areas for Contribution

We welcome contributions in these areas:

### High Priority
- New language support
- Additional game types
- Performance improvements
- Bug fixes

### Medium Priority
- UI/UX improvements
- Documentation enhancements
- Test coverage improvements

### Low Priority
- Code refactoring
- Minor feature enhancements

## 🤝 Community Guidelines

### Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and grow
- Follow the project's coding standards

### Communication

- Use clear, descriptive language
- Be patient with newcomers
- Ask questions if something is unclear
- Provide context in your contributions

## 🏆 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes for significant contributions
- Special thanks in documentation

## 📞 Getting Help

If you need help:
- Check existing issues and documentation
- Create a new issue with the "question" label
- Join our community discussions

## 🔄 Release Process

1. Features are merged into `develop` branch
2. Regular releases are cut from `develop` to `main`
3. Hotfixes go directly to `main` and are backported

Thank you for contributing to FillMyBlank.AI! 🎉
