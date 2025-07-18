# 📁 frontend/pages/home.py
import streamlit as st
from frontend.components.navbar import render_navbar
from frontend.components.footer import render_footer


def render_home():
    render_navbar()
    st.title("🎤 Welcome to FillMyBlank.ai")
    st.subheader("Unleash your voice, accent, memes & drama ✨")
    st.markdown("""
    Choose a challenge from the sidebar and start recording! 🎧📹

    🔊 Voice | 🎥 Acting | 💬 Fill-in-the-blank | 🧠 Creativity
    """)
    render_footer()


if __name__ == "__main__":
    render_home()
