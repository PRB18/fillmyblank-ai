import streamlit as st
from utils import auth, localization, storage, voice_to_text, leaderboard, feedback
from games import fill_in_blank, match_the_following, story_completion
import time

# Geolocation support
def get_geolocation():
    try:
        from streamlit_js_eval import streamlit_js_eval
        result = streamlit_js_eval(js_expressions="navigator.geolocation.getCurrentPosition((pos) => window.streamlitReceive({coords: pos.coords}))")
        lat, lon = "", ""
        if result and 'coords' in result:
            lat = result['coords'].get('latitude', '')
            lon = result['coords'].get('longitude', '')
        return lat, lon
    except Exception:
        return "", ""

def main():
    st.set_page_config(page_title="Duolingo-Style Multilingual App", layout="wide", page_icon="🦜")
    storage.initialize_csvs()
    auth.initialize_user_csv()
    feedback.initialize_feedback()

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = ""

    # Handle Hugging Face API key from secrets
    try:
        hugging_face_api_key = st.secrets["HUGGING_FACE_API_KEY"]
    except (KeyError, FileNotFoundError):
        hugging_face_api_key = ""  # Fallback to empty string if not found

    # Auth block
    if not st.session_state.logged_in:
        col1, col2 = st.columns([2,1])
        with col1:
            st.markdown("## 👋 Welcome! Log in or register to start your language journey.")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Login"):
                if auth.authenticate_user(username, password):
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success(f"Welcome {username}!")
                    st.rerun()
                else:
                    st.error("Invalid username or password")
            st.divider()
            new_username = st.text_input("New Username")
            new_password = st.text_input("New Password", type="password")
            avatar_url = st.text_input("Avatar URL (optional)", value=f"https://api.dicebear.com/7.x/identicon/svg?seed={username}")
            if st.button("Register"):
                ok, msg = auth.register_user(new_username, new_password, avatar_url)
                st.info(msg)
        with col2:
            st.image("https://cdn-icons-png.flaticon.com/512/616/616508.png", width=200)
        return

    # Main App
    username = st.session_state.username
    st.sidebar.header("Menu")
    avatar_url = auth.get_avatar(username)
    st.sidebar.image(avatar_url, width=64)
    lang = st.sidebar.selectbox(
        "Choose Language / भाषा / భాష",
        ["en", "hi", "te"],
        format_func=lambda x: {"en":"English", "hi":"हिंदी", "te":"తెలుగు"}[x]
    )
    section = st.sidebar.radio("Section", ["Play Game", "Dashboard", "Leaderboard", "Feedback"])
    if st.sidebar.button("Logout"):
        st.session_state.clear()
        st.rerun()

    st.sidebar.markdown("---")
    st.sidebar.markdown("Made with ❤️ by [Your Team]")

    prompts = localization.get_prompts(lang)
    lat, lon = get_geolocation()

    if section == "Play Game":
        st.header("🎯 Language Games")
        with st.expander("See Instructions"):
            st.info(
                "Select a game, answer the question (by text or voice), and let the AI check your answer!"
            )
        game_type = st.selectbox("Choose Game Type", ["Fill in the Blank", "Match the Following", "Story Completion"])
        if game_type == "Fill in the Blank":
            # Dynamic questions are now generated within the game
            user_answer, correct, transcript, audio_path, score_resp = fill_in_blank.play(None, lang, hugging_face_api_key)
            prompt = "Dynamic Fill-in-Blank Question"
        elif game_type == "Match the Following":
            # Dynamic questions are now generated within the game
            user_answer, correct = match_the_following.play(None, lang, hugging_face_api_key)
            transcript, audio_path, score_resp = "", "", ""
            prompt = "Dynamic Matching Exercise"
        else:
            # Dynamic questions are now generated within the game
            user_answer, correct = story_completion.play(None, lang, hugging_face_api_key)
            transcript, audio_path, score_resp = "", "", ""
            prompt = "Dynamic Story Completion"

        if st.button("Submit Response", key="submitresp"):
            storage.save_response(
                username=username,
                language=lang,
                game_type=game_type,
                prompt=prompt,
                response=user_answer,
                correct=correct,
                transcript=transcript,
                audio_file=audio_path,
                lat=lat,
                lon=lon
            )
            storage.update_leaderboard(username)
            st.success("Saved! Your participation is counted.")

    elif section == "Dashboard":
        st.header("📊 Your Progress")
        user_data = storage.get_user_data(username)
        st.metric("Total Attempts", len(user_data))
        st.dataframe(user_data)
        st.download_button("Download My Submissions", user_data.to_csv(index=False), "my_responses.csv")

    elif section == "Leaderboard":
        st.header("🏆 Leaderboard")
        df = leaderboard.get_leaderboard()
        st.dataframe(df)
        if username in df["username"].values:
            rank = df[df["username"] == username].index[0] + 1
            st.success(f"Your current rank: {rank}")

    elif section == "Feedback":
        st.header("💡 Feedback / Bug Report")
        fb = st.text_area("Describe your feedback or bug")
        if st.button("Submit Feedback"):
            feedback.save_feedback(username, fb)
        st.success("Thank you! Your feedback has been recorded.")
if __name__ == "__main__":
    main()

