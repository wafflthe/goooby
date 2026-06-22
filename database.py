import sqlite3

conn = sqlite3.connect("ideas.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS ideas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT NOT NULL,
        idea TEXT NOT NULL
    )
""")
conn.commit()
conn.close()

def init_db():
    conn = sqlite3.connect("ideas.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ideas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            idea TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def add_idea(idea, user_id):
    conn = sqlite3.connect("ideas.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO ideas (user_id, idea) VALUES (?, ?)", (user_id, idea)
    )
    conn.commit()
    conn.close()

def get_ideas(user_id):
    conn = sqlite3.connect("ideas.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT idea FROM ideas WHERE user_id = ? ORDER BY id", (user_id,)
    )
    ideas = cursor.fetchall()
    conn.close()
    return [r[0] for r in ideas]

def del_idea(id):
    conn = sqlite3.connect("ideas.db")
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM ideas WHERE id = ?", (id,)
    )
    conn.commit()
    conn.close()