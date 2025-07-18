# 📁 frontend/pages/play.py
import streamlit as st
import random
import os
import uuid
from datetime import datetime
from frontend.components.navbar import render_navbar
from frontend.components.footer import render_footer

# Challenge definitions
CHALLENGES = {
    "Meme Caption": {
        "type": "text",
        "prompts": [
            "When your code finally works but you don’t know why…",
            "Trying to act cool in front of your crush but tripping on air."
        ]
    },
    "Audio Acting": {
        "type": "audio",
        "prompts": [
            "Say ‘Oh really?’ like you're sarcastic and slightly offended.",
            "Yell ‘I'm done!’ like you're absolutely frustrated."
        ]
    },
    "Video Skit": {
        "type": "video",
        "prompts": [
            "Pretend you're explaining why you were late to class in a dramatic way.",
            "React to a meme where your crush likes your 2019 selfie."
        ]
    },
    "Fill the Blank (Spoken)": {
        "type": "audio",
        "prompts": [
            "When I saw my result, I...",
            "If I could teleport, the first place I’d go is..."
        ]
    },
    "Accent Challenge": {
        "type": "audio",
        "prompts": [
            "Say ‘I’m hungry’ in your native accent.",
            "Say ‘Let’s chill tomorrow’ using your own slang."
        ]
    },
    "Meme Reaction Skit": {
        "type": "video",
        "prompts": [
            "React to: when your laptop crashes just before saving.",
            "React to: seeing a pizza delivery guy when you're broke."
        ]
    }
}

# Helper to save data
def save_response(data, category, ext):
    folder = "responses"
    os.makedirs(folder, exist_ok=True)
    uid = uuid.uuid4().hex[:6]
    filename = f"{category.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uid}.{ext}"
    path = os.path.join(folder, filename)
    with open(path, "wb") as f:
        f.write(data)
    return filename

def render_play():
    render_navbar()
    st.title("🕹️ Play a Challenge")

    category = st.selectbox("Choose a Challenge:", list(CHALLENGES.keys()))
    challenge = CHALLENGES[category]
    prompt = random.choice(challenge["prompts"])

    st.markdown(f"### 🎯 Prompt: {prompt}")
    user = st.text_input("Your name (optional):")

    if challenge["type"] == "text":
        response = st.text_area("✍️ Your Caption")
        if st.button("Submit Caption") and response:
            data = f"Name: {user}\nCategory: {category}\nPrompt: {prompt}\nResponse: {response}\nTime: {datetime.now()}\n".encode()
            fname = save_response(data, category, "txt")
            st.success(f"Saved as {fname}")

    elif challenge["type"] == "audio":
        audio_data = st.audio_recorder("🎙️ Record your voice")
        if audio_data and st.button("Submit Audio"):
            fname = save_response(audio_data, category, "webm")
            st.success(f"Saved as {fname}")

    elif challenge["type"] == "video":
        st.markdown("📹 Upload your video skit (MP4/WebM)")
        video_file = st.file_uploader("Upload Video", type=["mp4", "webm"])
        if video_file and st.button("Submit Video"):
            fname = save_response(video_file.read(), category, video_file.name.split(".")[-1])
            st.success(f"Saved as {fname}")

    render_footer()

if __name__ == "__main__":
    render_play()
