# FillMyBlank.ai – Final Project Report

**Team:** LLMao
**Members:** Rishi, Sherlyn, Mahesh, Bhushan, Arshia
**App:** FillMyBlank.ai

---

##  1. User Acquisition & Growth Strategy (Primary Metric)

**Goal:** Reach 500+ real users in 2 weeks, generate 1k+ high-quality humorous/cultural data points.
**Plan:**

* **Phase 1: Soft Launch (Week 1)**

  * Target college meme pages, Reddit India threads, and Discord meme communities.
  * Incentivize responses with leaderboard-based shoutouts and a “Roast King” badge.
  * A/B test meme formats for engagement.

* **Phase 2: Viral Push (Week 2)**

  * Run meme-based Instagram story challenges ("Can you beat the AI at sarcasm?")
  * Collaborate with micro-creators (\~5K–50K followers) who can demo challenges.
  * Introduce challenge streaks to boost daily use.

**Measurement:**

* Daily active users
* Corpus points submitted
* Engagement per module
  *(Data collection is built-in real-time and timestamped.)*

---

##  2. Corpus Collection by Design

**Core Mechanism:** Users *must* generate creative text (meme replies, sarcasm completions, witty roast lines) to play the game.
**Every challenge is a disguised data annotation task.**
We collect:

* Indian English + Gen Z slang
* Sarcasm & humor context
* Meme logic and inference
* Timestamped and categorized submissions

**Corpus Quality Enhancers:**

* Optional meme image + user location for contextual accuracy
* Real-time AI feedback encourages users to “correct” or “improve” data

---

##  3. Accessibility & Performance

**Low-bandwidth First:**

* Built using **Streamlit** for fast mobile web delivery
* Lightweight backend via FastAPI
* Minimal external asset usage (CDNs avoided where possible)

**Offline Planning (In Progress):**

* LocalStorage fallback for unsent submissions
* Graceful retry logic when internet returns
* Designed to run on mobile browsers with poor connectivity

**Accessibility:**

* Text-based input only
* Screen-reader friendly layout (Streamlit default)
* No login required to try core modules (login only for leaderboard)

---

##  4. Team Collaboration Under Pressure

**Sprint Timeline:**

| Week     | Focus              | Output                                                    |
| -------- | ------------------ | --------------------------------------------------------- |
| Week 1   | Ideation + MVP Dev | App base setup, first challenge module                    |
| Week 2   | Testing + Growth   | User feedback loop, frontend polish, deployment           |
| Week 3-4 | Campaign           | Meme push, daily challenge rotation, analytics collection |

**Workflow:**

* GitLab Issues used to track every task
* Commits + MRs mapped to specific issues
* Daily updates on group chat + progress sync
* Clear division:

  * Rishi – Frontend
  * Sherlyn – AI model integration
  * Mahesh – Backend + Deployment
  * Bhushan – UI + Testing
  * Arshia – Content + Growth

---

##  5. AI Integration & Open-Source Adherence

**Strictly Open-Source Policy:**
No proprietary APIs used.
Model Plans:

* `tiiuae/falcon-7b`
* `mistralai/Mistral-7B-Instruct`
* Hugging Face Inference API used (self-hosted fallback planned)

**AI Usage in MVP:**

* Predicts sarcasm completion
* Ranks humor intensity
* Feedback loop improves user interaction *and* enhances data variety

---

##  6. Problem Understanding & MVP Elegance

**Problem:**
LLMs don’t get Indian humor, meme context, or sarcastic tone. They miss the vibe.

**Our Solution:**
Turn data collection into a fun, addictive game that *naturally* generates culturally rich, Gen Z-friendly data.

**Why It Works:**

* No boring data annotation forms
* No forced user behavior
* App = Game = Data

---

##  7. Report & Demo Quality

* **Live App Demo:** \[Hugging Face Space link – TBD]
* **Repo:** [GitLab – FillMyBlank.ai](#)
* **Docs:**

  * `README.md` – Full setup
  * `CHANGELOG.md` – Detailed commits
  * `CONTRIBUTING.md` – Guidelines
  * `LICENSE` – Open-source MIT
* **Demo Video:** \[YouTube link – TBD]

---

##  8. Post-Internship Vision

* **FillMyBlankGPT:** Fine-tune a lightweight LLM purely on Gen Z + Indian meme humor.
* **Open Corpus Release:** Community-curated humor dataset for downstream LLM research.
* **Scale Up:**

  * Add audio input (sarcastic voice tones)
  * Meme image generation from replies
  * Challenge-of-the-day via WhatsApp bot

---

##  9. Current Status (as of Week 1)

| Component                          | Status                             |
| ---------------------------------- | ---------------------------------- |
| Repo Setup                         | ✅                                 |
| Roles Assigned                     | ✅                                 |
| Frontend (Login + First Challenge) | 🚧                                 |
| Backend API                        | 🚧                                 |
| Deployment                         | 🚧                                  |
| Growth Campaign Prep               | ✅ (planned posts and assets ready) |

---

##  10. Meta Info

* **Geo Coordinates:** City + state via browser (opt-in)
* **User Info:** Email (optional), username
* **Corpus Categories:** Sarcasm, memes, roasts, blanks
* **Input Format:** Text (optional meme img)
* **Output Format:** Timestamped JSON
