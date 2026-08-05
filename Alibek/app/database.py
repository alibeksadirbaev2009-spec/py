import sqlite3

conn = sqlite3.connect("user.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
firstname TEXT NOT NULL,
lastname TEXT NOT NULL,
username TEXT NOT NULL UNIQUE,
age INTEGER NULL,
password TEXT NOT NULL
)
""")
conn.commit()
conn.close()

print("Database created!")
