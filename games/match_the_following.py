import streamlit as st
from utils.dynamic_questions import generate_dynamic_question

def play(prompt_data, lang, api_key):
    # Generate new question button
    if st.button("🎲 Generate New Question", key="new_question_mtf"):
        st.session_state.current_match_question = None
    
    # Get or generate current question
    if 'current_match_question' not in st.session_state or st.session_state.current_match_question is None:
        with st.spinner("🤖 AI is generating a new matching exercise..."):
            st.session_state.current_match_question = generate_dynamic_question("match_the_following", lang, api_key)
    
    question_data = st.session_state.current_match_question
    left = question_data["left"]
    right = question_data["right"]
    answer = question_data["answer"]
    
    st.write("🔗 **Match the following:**")
    st.caption("💡 Tip: Click 'Generate New Question' for a fresh challenge!")
    matchings = []
    for i, l_item in enumerate(left):
        idx = st.selectbox(f"{l_item}:", right, key=f"match-{l_item}")
        matchings.append(right.index(idx))
    correct = matchings == answer
    if st.button("Check Matches", key="mtf"):
        st.success("✅ Correct!" if correct else "❌ Wrong!")
    return str(matchings), correct