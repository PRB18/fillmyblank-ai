

### FillMyBlank.ai Project Report

> Team: **LLMao**
> Members: Rishi, Sherlyn, Mahesh, Bhushan, Arshia
> App: **FillMyBlank.ai**



### 1. Project Overview

**FillMyBlank.ai** is an AI-powered web application that offers interactive challenges like:

* Meme-based fill-in-the-blank quizzes
* Contextual wordplay puzzles
* Sarcastic reply prediction
* Conversational trolling & wit-based games

The core idea is to collect engaging user-generated data through fun challenges to improve LLM fine-tuning in Indian English and Gen Z slang.

---

### 2. Motivation

Current LLMs lack regional humor, sarcasm understanding, and meme context. Our app aims to crowdsource diverse, culturally rich, and funny data that can improve chatbots' sense of humor, meme literacy, and vibe matching.

---

### 3. Target Output / Deliverables

* A working **web app with login functionality**
* Challenge modules (fill-in-the-blank, meme reaction, sarcasm detection)
* Real-time data collection in JSON
* Export mechanism for collected data
* GitLab repo with proper issue tracking, branches, and commits
* Full documentation with change logs and license

---

### 4. Features (To Be Built)

* [ ] User Login System (OAuth optional)
* [ ] Meme-based blank-filling challenge
* [ ] Sarcastic sentence prediction challenge
* [ ] Leaderboard & scoring
* [ ] Real-time feedback on AI predictions
* [ ] Geo-coordinates collection (for regional data analysis)
* [ ] Download/export user responses as corpus

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

### 6. Geo Coordinates (Planned)

* We plan to collect **basic location info** (city, state) using browser geolocation API.
* This helps in regional language processing and understanding humor across zones.

---

### 7. Corpus Categories (Planned)

* Meme replies
* Fill-in-the-blanks
* Sarcasm completion
* Roast & banter responses
* Desi-English humor

Each user submission is categorized and timestamped.

---

### 8. GitLab Usage

* Multiple branches for frontend, backend, and challenge modules
* Merge Requests used for collaboration
* Issues created for each feature/bug
* Commits linked to tasks (following best practices)

---

### 9. API Strategy

* Only **open-source AI APIs** will be used (e.g., Hugging Face transformers)
* We avoid using proprietary APIs like OpenAI
* Plan to integrate pre-trained text-generation models (like `tiiuae/falcon`, `mistralai/Mistral-7B`, etc.)

---

### 10. Future Roadmap

* [ ] Fine-tune collected data into a humorous LLM (FillMyBlankGPT)
* [ ] Build an open-source dataset
* [ ] Add voice/mic input and meme uploads

---

### 11. Current Status

Project is in ideation & setup phase.

* Team setup ✅
* Repo initialized ✅
* Readme prepared ✅
* Roles divided 🔜
* First branch (`login-page`) will be created by Rishi

---

### 12. Changelog

See [`CHANGELOG.md`](./CHANGELOG.md)

---

### 13. Contributing

See [`CONTRIBUTING.md`](./CONTRIBUTING.md)

---

### 14. License

See [`LICENSE`](./LICENSE)

---

### 15. Meta Info

**Geo Coordinates**: Will be collected via browser
**User Info**: Email, city, username (optional)
**Corpus Categories**: Humor, memes, sarcasm, roasts
**Input Format**: Text (plus optional meme img for context)
**Output Format**: JSON dataset

---


