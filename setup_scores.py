import sqlite3

conn = sqlite3.connect("princespark.db")
c = conn.cursor()

# Create scores table if not exists
c.execute('''
CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    score INTEGER NOT NULL,
    quiz_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()
conn.close()

print("✅ Scores table created successfully!")
