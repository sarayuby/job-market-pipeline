import requests
import pandas as pd

def extract_data():
    url = "https://www.themuse.com/api/public/jobs?page=1"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("API failed")

    return response.json()



def transform_data(data):
    df = pd.DataFrame(data["results"])

    # ---- CLEAN COMPANY ----
    df["company_name"] = df["company"].apply(lambda x: x.get("name") if isinstance(x, dict) else None)

    # ---- CLEAN LOCATION ----
    df["location"] = df["locations"].apply(lambda x: x[0]["name"] if isinstance(x, list) and len(x) > 0 else None)

    # ---- CLEAN CATEGORY ----
    df["category"] = df["categories"].apply(lambda x: x[0]["name"] if isinstance(x, list) and len(x) > 0 else None)

    # ---- CLEAN LEVEL ----
    df["level"] = df["levels"].apply(lambda x: x[0]["name"] if isinstance(x, list) and len(x) > 0 else None)

    df["skills"] = df["contents"].apply(extract_skills)

    # ---- REDUCE TO USEFUL COLUMNS ----
    df_clean = df[[
    "name",
    "company_name",
    "location",
    "category",
    "level",
    "publication_date",
    "skills"
]]

    print(df_clean.head())

    return df_clean


from database.db import create_connection, create_tables

def load_data(df):
    conn = create_connection()
    create_tables(conn)

    cursor = conn.cursor()

    for _, row in df.iterrows():

        # Insert job
        cursor.execute("""
        INSERT INTO jobs
        (name, company_name, location, category, level, publication_date)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            row["name"],
            row["company_name"],
            row["location"],
            row["category"],
            row["level"],
            row["publication_date"]
        ))

        # Get the ID of the job we just inserted
        job_id = cursor.lastrowid

        print("Skills for this row:", row["skills"])

        # Insert skills
        for skill in row["skills"]:
            print("Inserting:", skill)

            cursor.execute("""
            INSERT INTO skills (job_id, skill)
            VALUES (?, ?)
            """, (job_id, skill))

    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM skills")
    print("Skills count:", cursor.fetchone())

    conn.close()

    print("Saved data to SQLite database (job_market.db)")




import re

def extract_skills(text):
    if not isinstance(text, str):
        return []

    skills = [
        "python", "sql", "aws", "spark", "airflow",
        "tableau", "excel", "machine learning",
        "pandas", "numpy", "snowflake"
    ]

    found = []
    text_lower = text.lower()

    for skill in skills:
        if skill in text_lower:
            found.append(skill)

    return found

def main():
    data = extract_data()

    df = transform_data(data)

    load_data(df)


if __name__ == "__main__":
    main()