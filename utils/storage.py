import pandas as pd
import os
import csv
from datetime import datetime

# Use /tmp directory for writable storage in deployment environments
DATA_DIR = "/tmp" if os.path.exists("/tmp") else "."
RESPONSES = os.path.join(DATA_DIR, "responses.csv")
LEADERBOARD = os.path.join(DATA_DIR, "leaderboard.csv")

def initialize_csvs():
    if not os.path.exists(RESPONSES):
        with open(RESPONSES, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "username", "language", "game_type", "prompt", "response", "correct",
                "transcript", "audio_file", "latitude", "longitude", "timestamp"
            ])
    if not os.path.exists(LEADERBOARD):
        with open(LEADERBOARD, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["username", "participation_count"])

def save_response(username, language, game_type, prompt, response, correct, transcript, audio_file, lat, lon):
    initialize_csvs()
    with open(RESPONSES, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            username, language, game_type, prompt, response, correct,
            transcript, audio_file, lat, lon, datetime.now().isoformat()
        ])

def update_leaderboard(username):
    initialize_csvs()
    df = pd.read_csv(LEADERBOARD)
    if username in df['username'].values:
        df.loc[df['username'] == username, 'participation_count'] += 1
    else:
        df.loc[len(df)] = [username, 1]
    df.to_csv(LEADERBOARD, index=False)

def get_user_data(username):
    initialize_csvs()
    df = pd.read_csv(RESPONSES)
    return df[df['username'] == username]