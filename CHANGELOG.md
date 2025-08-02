# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Project compliance files (pyproject.toml, VSCode config, GitLab templates)
- Comprehensive documentation (README, CONTRIBUTING, CHANGELOG)
- Development tooling setup (Ruff, Black, pytest configuration)

## [1.0.0] - 2024-XX-XX

### Added
- Initial release of FillMyBlank.AI by development team
- Streamlit-based web application (Arshia - Frontend)
- User authentication system with bcrypt (Sherlyn - Backend)
- Multiple language learning games:
  - Fill in the blank exercises
  - Matching games
  - Story completion challenges
- Voice input functionality using SpeechRecognition
- AI-powered language processing with Llama API
- Multilingual support with translation capabilities
- User leaderboard and progress tracking
- CSV-based data storage for users, responses, and feedback

### Features
- Interactive web interface built with Streamlit
- Real-time speech recognition for pronunciation practice
- AI-generated content and responses
- Multi-language support with indic-transliteration
- User progress tracking and gamification
- Responsive design for various screen sizes

### Technical
- Python-based backend with modular architecture
- Integration with external AI APIs
- Audio processing capabilities
- Secure user authentication
- File-based data persistence

### Dependencies
- streamlit>=1.31.0
- speechrecognition
- transformers
- sentence-transformers
- pandas
- bcrypt
- requests
- pydub
- soundfile
- streamlit-js-eval
- indic-transliteration

## [0.1.0] - 2024-XX-XX

### Added
- Initial project setup
- Basic Streamlit application structure
- Core game mechanics
- User authentication framework

---

## Release Notes Format

### Added
- New features

### Changed
- Changes in existing functionality

### Deprecated
- Soon-to-be removed features

### Removed
- Now removed features

### Fixed
- Bug fixes

### Security
- Security improvements
