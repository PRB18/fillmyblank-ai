# 📁 frontend/components/sidebar.py

import streamlit as st

def render_sidebar():
    st.sidebar.title("🧩 Challenges")
    st.sidebar.markdown("""
    - 🎤 Home  
    - 🎮 Play a Challenge  
    - 🏆 Leaderboard  
    """)
