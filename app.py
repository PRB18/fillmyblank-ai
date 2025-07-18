import streamlit as st
import random
import json
import os
import time
import requests

# Load or initialize leaderboard
LEADERBOARD_FILE = "leaderboard.json"
if not os.path.exists(LEADERBOARD_FILE):
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump([], f)

def load_leaderboard():
    with open(LEADERBOARD_FILE, "r") as f:
        return json.load(f)

def save_leaderboard(data):
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_random_prompt():
    prompts = [
        {"title": "Love Tweet", "text": "Love is like _____", "category": "Romance"},
        {"title": "Startup Meme", "text": "Our startup pitch was just _____", "category": "Humor"},
        {"title": "Bollywood Drama", "text": "Kabir Singh but with _____", "category": "Pop Culture"},
    ]
    return random.choice(prompts)

def get_ai_feedback(prompt, response, openrouter_api_key=None):
    if not openrouter_api_key:
        return {
            "score": random.randint(5, 10),
            "feedback": "This is a mock score. Add your OpenRouter API key for real feedback."
        }

    system_prompt = (
        "You are a witty but fair evaluator who scores fill-in-the-blank responses. "
        "Give a score out of 10 based on creativity, humor, and relevance, followed by a short comment."
    )

    user_prompt = f"Prompt: {prompt}\nUser's Completion: {response}\nScore and Comment:"

    try:
        res = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {openrouter_api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": "openai/gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "temperature": 0.7
            },
        )
        result = res.json()
        reply = result["choices"][0]["message"]["content"]
        score_line, *feedback_lines = reply.strip().split("\n")
        score = int("".join(filter(str.isdigit, score_line)) or 7)
        feedback = " ".join(feedback_lines).strip() or "Interesting!"
        return {"score": score, "feedback": feedback}

    except Exception as e:
        return {
            "score": random.randint(5, 10),
            "feedback": f"Could not fetch real feedback. Error: {str(e)}"
        }

# --- Streamlit UI ---
st.set_page_config(page_title="FillMyBlank.ai", layout="centered")
st.title("🎯 FillMyBlank.ai")
st.caption("Creativity, Humor, and AI Feedback — Let's Play!")

api_key = st.sidebar.text_input("🔑 OpenRouter API Key (Optional)", type="password")

st.markdown("## ✍️ Your Challenge")
prompt = get_random_prompt()
st.write(f"**{prompt['title']}**")
st.info(prompt['text'])

def load_custom_css():
    with open("frontend/styling/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Call it before any render functions
load_custom_css()


user_input = st.text_input("Your Response:", placeholder="Type your witty/funny reply here...")

if st.button("Submit"):
    if not user_input.strip():
        st.warning("Please enter a response!")
    else:
        with st.spinner("Scoring your brilliance..."):
            result = get_ai_feedback(prompt['text'], user_input, openrouter_api_key=api_key)
            st.success(f"🎉 Score: {result['score']}/10")
            st.write(f"🧠 AI Feedback: *{result['feedback']}*")

            name = st.text_input("Enter your name for the leaderboard:", key="name_entry")
            if name:
                leaderboard = load_leaderboard()
                leaderboard.append({
                    "name": name,
                    "score": result['score'],
                    "response": user_input,
                    "prompt": prompt['text'],
                    "timestamp": time.time()
                })
                save_leaderboard(leaderboard)
                st.success("✅ Submitted to leaderboard!")

st.markdown("---")
st.markdown("## 🏆 Leaderboard (Top Scores)")
lb_data = load_leaderboard()
sorted_lb = sorted(lb_data, key=lambda x: x["score"], reverse=True)[:5]
for idx, entry in enumerate(sorted_lb, 1):
    st.write(f"{idx}. **{entry['name']}** - {entry['score']}/10")
