import sqlite3

# Connect (this will create princespark.db if it doesn't exist)
conn = sqlite3.connect("princespark.db")
c = conn.cursor()

# ---------------- Users table ----------------
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    score INTEGER DEFAULT 0
)
""")

# ---------------- Questions table ----------------
c.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option1 TEXT NOT NULL,
    option2 TEXT NOT NULL,
    option3 TEXT NOT NULL,
    option4 TEXT NOT NULL,
    answer INTEGER NOT NULL
)
""")

# ---------------- Insert sample user ----------------
try:
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("rishav", "1234"))
except sqlite3.IntegrityError:
    pass  # user already exists

# ---------------- Insert sample questions ----------------
sample_questions = [
    ("What is 2 + 2?", "3", "4", "5", "6", 2),
    ("Capital of India?", "Delhi", "Mumbai", "Kolkata", "Chennai", 1),
    ("Which planet is known as Red Planet?", "Earth", "Mars", "Venus", "Jupiter", 2)
]

for q in sample_questions:
    try:
        c.execute("INSERT INTO questions (question, option1, option2, option3, option4, answer) VALUES (?, ?, ?, ?, ?, ?)", q)
    except sqlite3.IntegrityError:
        pass

conn.commit()
conn.close()

print("✅ Database setup complete with sample user & questions!")
