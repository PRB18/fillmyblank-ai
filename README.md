# FillMyBlank.ai


**FillMyBlank.ai** is an AI-powered web app that challenges users to complete memes, tweets, or short quotes using their creativity. The AI provides real-time feedback, scores, and even generates new challenges — combining fun, wit, and intelligence in a gamified social platform.


## 🔹 Project Overview

FillMyBlank.ai is designed to promote creative expression using generative AI. It focuses on language, culture, and community engagement through humor and wit. The user is shown incomplete or blank memes, quotes, or short tweets and challenged to complete them in a meaningful or funny way.

The application evaluates the response, provides feedback, and updates the leaderboard accordingly.

---

## 🔹 Core Features

### 1. Interactive Challenges  
Users receive fill-in-the-blank prompts in the form of memes, tweets, or short quotes.

### 2. Real-time AI Feedback  
The AI rates responses based on humor, creativity, and relevance.

### 3. Leaderboard  
Scores are tracked in real-time and shown to encourage competitive fun.

### 4. Content Generation  
The AI can create new incomplete sentences using templates and style transfer.

### 5. User Login System 
We plan to introduce a secure user login page to track individual performance and history.

### 6. Geo-based Trend Analysis
If users give consent, their location (geo-coordinates) will be collected to analyze regional trends in humor and creativity. This feature will be entirely optional.

### 7. Corpus Categorization  
Each prompt submitted by the community will include:
- A **title**
- A **description**
- A **category** (e.g., humor, politics, pop culture)

These inputs will be used to build an evolving, community-driven prompt corpus for future generations of FillMyBlank challenges.

---
## 🔹 Folder Structure

<pre>

FillMyBlank.ai/
├── .gitignore
├── LICENSE
├── README.md
├── report.md
├── requirements.txt
├── CHANGELOG.md
├── CONTRIBUTING.md
├── ISSUE_TEMPLATE/
│   ├── bug_report.md
│   └── feature_request.md
├── .gitlab/
│   └── metadata.yml
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── auth/
│   │   ├── login.py
│   │   └── register.py
│   ├── challenges/
│   │   ├── fill_in_the_blank.py
│   │   ├── word_unscramble.py
│   │   └── meme_caption.py
│   ├── utils/
│   │   ├── ai_api.py              
│   │   └── helpers.py
│   ├── static/
│   │   └── styles.css
│   └── templates/
│       ├── index.html
│       ├── login.html
│       ├── dashboard.html
│       └── challenge.html
├── data/
│   ├── raw/
│   └── processed/
├── scripts/
│   └── data_cleaner.py
└── docs/
    ├── architecture_diagram.png
    ├── er_model.png
    └── usage_guide.md

</pre>

---

## 🔹 Tech Stack

| Component        | Technology Used                      |
|------------------|--------------------------------------|
| **Frontend**      | Streamlit (Python-based UI)          |
| **Backend**       | Python (FastAPI or Flask - planned)  |
| **AI Model**      | OpenRouter API (OpenAI/Groq backend) |
| **Version Control** | GitLab                              |
| **Deployment**    | Hugging Face Spaces (or Render)      |
| **Team Workflow** | GitLab Issues, Commits, Merge Requests |

---

## 🔹 Corpus Submission Details

We plan to collect a categorized prompt dataset from users and ourselves. Each entry will have:
- **Title**: A brief heading of the prompt  
- **Description**: Detailed context or backstory  
- **Category**: The theme of the prompt (e.g., Satire, Love, News, Pop, GenZ)

This structure will allow us to analyze and use prompts more intelligently in the future — for search, filtering, and personalization.

---

## 🔹 Progress & Versioning

We are actively using **GitLab** for project management:
- Each feature is tracked using GitLab Issues
- Commits follow semantic structure
- Merge Requests are reviewed collaboratively

We will add changelogs and version tagging once the MVP is finalized.

---

## 🔹 Future Plans

- Add login system with session tracking
- Enable multiplayer challenge mode
- Add support for Telugu and other regional languages
- Create mobile-first UI using React or Flutter (Phase 2)
- Integrate personalized meme generation using image captioning models

---

## 🔹 Contributors' Roles

| Member   | Role             | Contributions |
|----------|------------------|---------------|
| Sherlyn  | UI/UX Designer   | Streamlit layout, styling |
| Mahesh   | Backend Lead     | Flask API design, model integration |
| Bhushan  | Prompt Engineer  | Corpus design, category strategy |
| Arshia   | Feature Developer| AI feedback system |
| Rishi    | Project Lead     | Architecture, README, issue tracking, integration |

---

## 🔹 Ethical Statement

All AI-generated responses and feedback are filtered to avoid hate speech, offensive content, or misinformation. Geo-location tracking will be strictly opt-in and anonymized for trend purposes only.

---

## 🔹 Contact

- For issues, ideas, or collaboration requests, open an Issue in this repo or contact any team member directly through GitLab.
- For prompt dataset contributions, please fill out the Google Form (to be shared).

---

## 🔹 License

This project is licensed under **MIT License**. See `LICENSE.md` for full details.

---

## 🔹 Deployment

- The project will be deployed to **Hugging Face Spaces** or **Render** after MVP completion.
- A public URL will be shared here once the app is live.

---
>This README represents our current vision and implementation plan for FillMyBlank.ai, submitted as part of the hackathon project under Swecha/WikiVerse.