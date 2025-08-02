import pandas as pd
import bcrypt
import os

# Use /tmp directory for writable storage in deployment environments
DATA_DIR = "/tmp" if os.path.exists("/tmp") else "."
USERS_CSV = os.path.join(DATA_DIR, "users.csv")

def initialize_user_csv():
    if not os.path.exists(USERS_CSV):
        df = pd.DataFrame(columns=['username', 'password_hash', 'avatar_url'])
        df.to_csv(USERS_CSV, index=False)

def register_user(username, password, avatar_url=None):
    initialize_user_csv()
    df = pd.read_csv(USERS_CSV)
    if username in df['username'].values:
        return False, "Username already exists"
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    new_user = pd.DataFrame([[username, hashed.decode(), avatar_url or "https://api.dicebear.com/7.x/identicon/svg?seed="+username]], columns=df.columns)
    df = pd.concat([df, new_user], ignore_index=True)
    df.to_csv(USERS_CSV, index=False)
    return True, "Registration successful!"

def authenticate_user(username, password):
    initialize_user_csv()
    df = pd.read_csv(USERS_CSV)
    row = df[df['username'] == username]
    if row.empty:
        return False
    stored = row['password_hash'].iloc[0].encode()
    return bcrypt.checkpw(password.encode(), stored)

def get_avatar(username):
    df = pd.read_csv(USERS_CSV)
    row = df[df['username'] == username]
    if not row.empty:
        return row['avatar_url'].iloc[0]
    return "https://api.dicebear.com/7.x/identicon/svg?seed="+username