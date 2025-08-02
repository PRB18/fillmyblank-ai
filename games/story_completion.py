import streamlit as st
from utils.llm_score import llama_score_sentence
from utils.dynamic_questions import generate_dynamic_question

def play(prompt_data, lang, api_key):
    # Generate new question button
    if st.button("🎲 Generate New Question", key="new_question_story"):
        st.session_state.current_story_question = None
    
    # Get or generate current question
    if 'current_story_question' not in st.session_state or st.session_state.current_story_question is None:
        with st.spinner("🤖 AI is generating a new story..."):
            st.session_state.current_story_question = generate_dynamic_question("story_completion", lang, api_key)
    
    question_data = st.session_state.current_story_question
    story = question_data["story"]
    answer = question_data["answer"]
    
    st.caption("💡 Tip: Click 'Generate New Question' for a fresh challenge!")
    user_answer = st.text_input(story)
    correct = None
    if st.button("Check Answer", key=f"story-{story}"):
        user_input = user_answer.strip().lower()
        correct_answer = answer.strip().lower()
        
        # Simple text comparison scoring (more reliable than API)
        if user_input == correct_answer:
            st.success("✅ Correct! Well done!")
            correct = True
        elif user_input in correct_answer or correct_answer in user_input:
            st.success("✅ Very close! That's correct!")
            correct = True
        else:
            st.error(f"❌ Not quite! The correct answer is: **{answer}**")
            correct = False
    return user_answer, correct