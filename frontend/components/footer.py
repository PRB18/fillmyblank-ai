# 📁 frontend/components/footer.py

import streamlit as st

def render_footer():
    st.markdown("""
        <style>
            .footer {
                margin-top: 2rem;
                padding-top: 1rem;
                border-top: 1px solid #ccc;
                text-align: center;
                font-size: 0.9rem;
                color: gray;
            }
        </style>
        <div class="footer">
            Made with ❤️ by Team FillMyBlank.ai
        </div>
    """, unsafe_allow_html=True)
