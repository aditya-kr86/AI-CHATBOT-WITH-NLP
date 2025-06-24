import sqlite3
from datetime import datetime
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def init_db(db_path="chat_log.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS chatlog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            user_input TEXT,
            bot_response TEXT,
            intent TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_chat(user_input, bot_response, intent, db_path="chat_log.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO chatlog (timestamp, user_input, bot_response, intent)
        VALUES (?, ?, ?, ?)
    ''', (datetime.now().isoformat(), user_input, bot_response, intent))
    conn.commit()
    conn.close()
