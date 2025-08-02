import streamlit as st
from utils.voice_to_text import transcribe_audio
from utils.llm_score import llama_score_sentence
from utils.dynamic_questions import generate_dynamic_question

def play(prompt_data, lang, api_key):
    st.subheader("📝 Fill in the Blank")
    
    # Generate new question button
    if st.button("🎲 Generate New Question", key="new_question_fib"):
        st.session_state.current_question = None
    
    # Get or generate current question
    if 'current_question' not in st.session_state or st.session_state.current_question is None:
        with st.spinner("🤖 AI is generating a new question..."):
            st.session_state.current_question = generate_dynamic_question("fill_in_blank", lang, api_key)
    
    question_data = st.session_state.current_question
    prompt = question_data["prompt"]
    answer = question_data["answer"]
    
    st.markdown(f"**{prompt}**")
    st.caption("💡 Tip: Click 'Generate New Question' for a fresh challenge!")

    user_answer = st.text_input("Type your answer:")
    audio_bytes = st.file_uploader("Or record your answer:", type=['wav', 'ogg'])

    transcript = ""
    audio_path = ""
    if audio_bytes:
        audio_path = f"audio_fib_{st.session_state.username}_{prompt[:5]}.wav"
        transcript = transcribe_audio(audio_bytes.read(), audio_path)
        st.write(f"Transcript: {transcript}")

    result = None
    if st.button("Check My Answer"):
        user_input = (user_answer or transcript).strip().lower()
        correct_answer = answer.strip().lower()
        
        # Simple text comparison scoring (more reliable than API)
        if user_input == correct_answer:
            st.success("✅ Correct! Well done!")
            result = True
            score_resp = "Correct"
        elif user_input in correct_answer or correct_answer in user_input:
            st.success("✅ Very close! That's correct!")
            result = True
            score_resp = "Close match - Correct"
        else:
            st.error(f"❌ Not quite! The correct answer is: **{answer}**")
            result = False
            score_resp = f"Incorrect. Correct answer: {answer}"
        
        return user_answer or transcript, result, transcript, audio_path, score_resp
    return user_answer or transcript, None, transcript, audio_path, None