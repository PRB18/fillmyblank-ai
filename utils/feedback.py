import os
import csv
from datetime import datetime

# Use /tmp directory for writable storage in deployment environments
DATA_DIR = "/tmp" if os.path.exists("/tmp") else "."
FEEDBACK = os.path.join(DATA_DIR, "feedback.csv")

def initialize_feedback():
    if not os.path.exists(FEEDBACK):
        with open(FEEDBACK, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["username", "feedback", "timestamp"])

def save_feedback(username, feedback):
    initialize_feedback()
    with open(FEEDBACK, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([username, feedback, datetime.now().isoformat()])