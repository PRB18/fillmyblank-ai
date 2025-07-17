# 🧠 FillMyBlank.exe  
### 🚀 By Team LLMao  
Sherlyn, Mahesh, Bhushan, Arshia, Rishi  

> _"An AI-Powered Challenge Arena for the Short-Attention-Span Generation."_

---

## 🎯 Project Summary

**FillMyBlank.exe** is a fun, fast-paced, and socially engaging web application built for Gen-Z users who crave interactivity, humour, and competition. The platform features **a set of meme-style AI challenges** — from fill-in-the-blanks to vibe-matching and meme-completion — where users test their wit, creativity, and timing.

Our unique twist? The AI doesn't just sit back — it actively judges the responses, scores them, and adapts to user humor over time. As users play, **we collect sentence-level data enriched with metadata** to fine-tune our open-source language model for better contextual understanding of Gen-Z tone, humor, and vibes.

---

## 💡 Why This?

Most LLM hackathon projects are just chatbots in disguise. We're different.  
We focused on:
- **Engagement over utility**
- **Humor over formality**
- **Data creation over consumption**

We aim to **combat attention fatigue** and make AI feel fun and approachable again — all while **collecting usable, fresh data** to fine-tune an open-source model.

---

## 🎮 Core Features

| 🧪 Challenge Type      | Description |
|------------------------|-------------|
| ✍️ Fill in the Blank   | User completes a quirky or sarcastic sentence. AI rates it based on humor, tone, and relevance. |
| 📸 Meme Completion     | User writes captions for partially completed memes. AI ranks wittiness. |
| 🧠 Vibe Match          | Match a sentence to the correct vibe (funny, sad, sarcastic). AI checks alignment. |
| 🤖 Judge's Verdict     | AI gives feedback, humor score, and leaderboard placement for each challenge.|

---

## 📦 Tech Stack

| Layer       | Tech Used |
|-------------|-----------|
| 👩‍🎨 Frontend   | Streamlit (for rapid prototyping), Tailwind CSS (if needed), HTML/CSS |
| 🧠 AI Backend | Sentence Transformers (`all-MiniLM-L6-v2`), Open Source LLMs (`phi`, `gemma`, `mistral`) |
| 🗃️ Data Layer  | JSONL / SQLite (for corpus and response metadata storage) |
| 🚀 Hosting    | Hugging Face Spaces / Streamlit Cloud |
| 🛠️ DevOps     | GitLab CI/CD, Python venv, Docker (optional) |

---

## 🔐 Data Handling & Structure

We collect the following metadata along with each user submission:

| Field             | Description |
|------------------|-------------|
| `user_id`         | Anonymous user identifier (hashed or UUID) |
| `timestamp`       | Time of submission (UTC) |
| `geo_coordinates` | Optional latitude and longitude (with user consent) |
| `title`           | Title of the user-generated challenge or meme |
| `description`     | Short description/context of the prompt |
| `category`        | Type of challenge: `"Blank"`, `"Meme"`, or `"Vibe"` |
| `response`        | User-submitted text |
| `ai_score`        | AI-generated humor/context relevance score |
| `judge_feedback`  | Qualitative feedback given by the AI |

> Data is stored in `.jsonl` format and anonymized to protect user privacy.

### 📝 Sample Data Entry

```json
{
  "user_id": "a3d9e90e-39f3-4bb1-944c-bc14c2b1d62a",
  "timestamp": "2025-07-17T10:24:00Z",
  "geo_coordinates": {"lat": 17.385044, "lon": 78.486671},
  "title": "Meme Caption: Elon at Mars",
  "description": "Elon Musk landing on Mars meme - fill in the final dialogue",
  "category": "Meme",
  "response": "When you realize you left the stove on at Earth.",
  "ai_score": 8.2,
  "judge_feedback": "Nice twist! Sarcastic and relevant to the meme."
}
```
### 🧠 Model Usage

We use Sentence Transformers to compute semantic similarity and humor scoring via cosine similarity. Responses may also be labeled and used in future fine-tuning runs (classification tasks like "Funny", "Mid", "Dead").

All AI models used are fully open-source and comply with hackathon rules (no closed APIs like GPT-4).

📈 Long-Term Vision

    Build a public humor dataset from anonymous user input (CC0).

    Fine-tune a humor-aligned open-source LLM using HuggingFace PEFT.

    Support multimodal challenges (images + captions).

    Enable offline mode for privacy-conscious users.

🤝 Contribution Roles
Name	Role
Rishi	AI System Design, Prompt Engineering
Sherlyn	UI/UX Design, Challenge Ideation
Mahesh	Frontend Development
Arshia	Dataset Handling, User Flow Design
Bhushan	Model Integration, Backend Logic

🌍 License

This project is licensed under the MIT License.
User-generated content is collected under the Creative Commons Zero (CC0) license for public domain AI training purposes.


🧠 Final Words

This isn’t your average chatbot.
It’s "FillMyBlank.ai" — where creativity meets chaos, and AI learns to meme.

