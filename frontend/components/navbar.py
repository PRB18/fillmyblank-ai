# 📁 frontend/components/navbar.py

import streamlit as st

def render_navbar():
    st.markdown("""
        <style>
            .navbar {
                background-color: #111827;
                color: white;
                padding: 1rem;
                border-radius: 0.5rem;
                margin-bottom: 1.5rem;
                text-align: center;
                font-size: 1.2rem;
                font-weight: bold;
                letter-spacing: 1px;
            }
        </style>
        <div class="navbar">
            🚀 FillMyBlank.ai — Challenge Your Creativity
        </div>
    """, unsafe_allow_html=True)
