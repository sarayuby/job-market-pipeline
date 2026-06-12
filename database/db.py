import sqlite3

def create_connection():
    conn = sqlite3.connect("job_market.db")
    return conn


def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        company_name TEXT,
        location TEXT,
        category TEXT,
        level TEXT,
        publication_date TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS skills (
        job_id INTEGER,
        skill TEXT
    )
    """)

    conn.commit()