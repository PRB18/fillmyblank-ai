import streamlit as st
import soundfile as sf
import os
import datetime
from streamlit_mic_recorder import mic_recorder
import random

st.title("🧠 FillMyBlank.ai MVP")

st.markdown("### Type your answer, then speak it aloud!")

# Simple prompts list (you can later pull from CSV)
prompts = [
    "Zindagi ek ____ hai.",
    "I love eating ____ on Sundays.",
    "తెలుగు సినిమా అంటే నాకు ____ గుర్తుకొస్తుంది.",
    "The festival of ____ is my favorite.",
    "मेरे पापा हमेशा कहते हैं ____"
]

prompt = random.choice(prompts)
st.write(f"🔤 Prompt: **{prompt}**")

# Text answer
text_input = st.text_input("📝 Your filled-in sentence:")

# Audio recording
audio = mic_recorder(start_prompt="🎙️ Record your voice", stop_prompt="⏹️ Stop", key="recorder")

# Save data when both are present
if st.button("✅ Submit"):
    if not text_input or not audio:
        st.warning("Please fill in the blank and record your voice.")
    else:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename_base = f"user_input_{timestamp}"

        os.makedirs("submissions", exist_ok=True)

        # Save text
        with open(f"submissions/{filename_base}.txt", "w", encoding="utf-8") as f:
            f.write(f"Prompt: {prompt}\nResponse: {text_input}\n")

        # Save audio
        sf.write(f"submissions/{filename_base}.wav", audio["bytes"], samplerate=audio["sample_rate"])

        st.success("Your response has been submitted. Thanks!")
