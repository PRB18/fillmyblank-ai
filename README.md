# FillMyBlank.AI - Multilingual Language Learning App

A Streamlit-based multilingual language learning application with interactive games and AI-powered features.

## 🚀 Features

- **Interactive Games**: Fill in the blank, matching exercises, and story completion
- **Voice Input**: Speech recognition for pronunciation practice
- **Multilingual Support**: Support for multiple languages with AI translation
- **User Authentication**: Secure login and registration system
- **Leaderboard**: Track progress and compete with other learners
- **AI-Powered**: Uses Llama API for intelligent language processing

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **AI/ML**: Transformers, Sentence Transformers
- **Speech**: SpeechRecognition, PyDub
- **Authentication**: bcrypt
- **Data**: Pandas, CSV storage

## 📋 Prerequisites

- Python 3.8 or higher
- pip or uv package manager

## 🔧 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd fillmyblank-ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
# or using uv
uv sync
```

3. Set up environment variables:
   - Copy `secrets.toml.example` to `secrets.toml`
   - Configure your API keys and settings

## 🚀 Running the Application

```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## 🎮 How to Use

1. **Register/Login**: Create an account or log in with existing credentials
2. **Choose a Game**: Select from available language learning games
3. **Practice**: Complete exercises and improve your language skills
4. **Track Progress**: View your scores on the leaderboard

## 🏗️ Project Structure

```
├── app.py                 # Main Streamlit application
├── games/                 # Game modules
│   ├── fill_in_blank.py  # Fill in the blank game
│   ├── match_the_following.py # Matching game
│   └── ...
├── utils/                 # Utility modules
│   ├── leaderboard.py    # Leaderboard functionality
│   └── ...
├── assets/               # Static assets
│   └── prompts.json     # AI prompts
├── requirements.txt      # Python dependencies
├── pyproject.toml       # Project configuration
└── README.md           # This file
```

## 🤝 Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📝 License

This project is licensed under the AGPL-3.0 License - see the [LICENSE](LICENSE) file for details.

## 🐛 Bug Reports

If you find a bug, please create an issue using our [bug report template](.gitlab/issue_templates/Bug.md).

## 💡 Feature Requests

For feature requests, please use our [feature request template](.gitlab/issue_templates/Feature_Request.md).

## 📊 Development

### Code Quality

- **Linting**: Ruff
- **Formatting**: Black
- **Testing**: pytest

### VSCode Setup

This project includes VSCode configuration files in `.vscode/` for:
- Recommended extensions
- Debug configurations
- Task definitions
- Editor settings

## 🔗 Links

- [API Documentation](docs/api.md)
- [User Guide](docs/user-guide.md)
- [Developer Guide](docs/developer-guide.md)
