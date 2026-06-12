import sqlite3

conn = sqlite3.connect("job_market.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS skills (
    job_id INTEGER,
    skill TEXT
)
""")
# show tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cursor.fetchall())

# show some jobs
cursor.execute("SELECT * FROM jobs LIMIT 5;")
print("\nSample Jobs:")
for row in cursor.fetchall():
    print(row)

conn.close()