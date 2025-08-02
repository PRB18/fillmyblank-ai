import json
import os

ASSETS_DIR = os.path.join(os.path.dirname(__file__), '..', 'assets')
PROMPTS_FILE = os.path.join(ASSETS_DIR, 'prompts.json')

def get_prompts(language):
    with open(PROMPTS_FILE, "r", encoding="utf-8") as f:
        all_prompts = json.load(f)
    return all_prompts.get(language, all_prompts['en'])