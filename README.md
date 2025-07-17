# 🧠 FillMyBlank.exe  
### 🚀 By Team LLMao  
Sherlyn, Mahesh, Bhushan, Arshia, Rishi  


> _"An AI-Powered Challenge Arena for the Short-Attention-Span Generation."_

---

## 🎯 Project Summary

**FillMyBlank.exe** is a fun, fast-paced, and socially engaging web application built for Gen-Z users who crave interactivity, humour, and competition. The platform features **a set of meme-style AI challenges** — from fill-in-the-blanks to vibe-matching and meme-completion — where users test their wit, creativity, and timing.  

Our unique twist? The AI doesn't just sit back — it actively judges the responses, scores them, and adapts to user humor over time. As users play, **we collect sentence-level data** to fine-tune our open-source language model for better contextual understanding of Gen-Z tone, humor, and vibes.

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
| 👩‍🎨 Frontend   | Streamlit (for rapid prototyping), Tailwind CSS (if needed for style), HTML/CSS |
| 🧠 AI Backend | Sentence Transformers (`all-MiniLM-L6-v2`), Open Source LLMs (e.g., `phi`, `gemma`, `mistral`, etc. as fallback for scoring/judgment) |
| 🗃️ Data Layer  | SQLite or JSONL for collecting prompts and user responses |
| 🚀 Hosting    | Hugging Face Spaces or Streamlit Cloud |
| 🛠️ DevOps     | GitLab CI/CD, Python venv, Docker (optional) |

---

## 🔐 Data Handling

We collect the following:
- Anonymous responses per challenge (text only)
- AI-assigned scores
- Timestamp (optional)

This data helps us:
- Fine-tune the AI on humor and context
- Build a Gen-Z centric response dataset (CC0 open license)

---

## 🧠 Model Usage

We use **Sentence Transformers** to compute semantic similarity and humor scoring via cosine similarity. Optionally, we may fine-tune using the responses as supervised classification (e.g., "Funny", "Mid", "Dead").

All models used are **open-source** (no GPT-4 or closed APIs), following hackathon guidelines.

---

## 📈 Long-Term Vision

- Build a **public humor dataset** from anonymous user input.
- Create a **humor-aligned small LLM** fine-tuned using HuggingFace PEFT.
- Expand to include **multimodal inputs** (image + text caption rating).
- Add **offline local mode** for privacy-conscious users.

---

## 🤝 Contribution Roles

| Name     | Role             |
|----------|------------------|
| Rishi    | AI System Design, Prompt Engineering |
| Sherlyn  | UI/UX Design, Challenge Ideation |
| Mahesh   | Frontend Development |
| Arshia   | Dataset Handling, User Flow Design |
| Bhushan  | Model Integration, Backend Logic |

---

## 🌍 License

This project is licensed under **MIT**.  
User-generated content is collected under **Creative Commons Zero (CC0)** for AI training purposes.

---

## 🧠 Final Words

This isn’t your average chatbot.  
It’s **"FillMyBlank.exe"** — where **creativity meets chaos**, and AI learns to meme.

---
