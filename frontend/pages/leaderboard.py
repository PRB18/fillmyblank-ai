import streamlit as st
from frontend.components.navbar import render_navbar
from frontend.components.footer import render_footer

def render_leaderboard():
    render_navbar()
    st.title("🏆 Leaderboard")
    st.info("Leaderboard will appear here once scoring & feedback systems are integrated.")
    st.markdown("""
    In the future, this page will show:
    - Top submissions 🎖
    - Most creative audio/video entries 🎭
    - Community favorites 🌟
    """)
    render_footer()


if __name__ == "__main__":
    render_leaderboard()
