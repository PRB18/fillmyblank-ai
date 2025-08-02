import pandas as pd
import os

# Use /tmp directory for writable storage in deployment environments
DATA_DIR = "/tmp" if os.path.exists("/tmp") else "."
LEADERBOARD = os.path.join(DATA_DIR, "leaderboard.csv")

def get_leaderboard():
    if not os.path.exists(LEADERBOARD):
        return pd.DataFrame(columns=["username", "participation_count"])
    df = pd.read_csv(LEADERBOARD)
    df = df.sort_values(by="participation_count", ascending=False)
    return df