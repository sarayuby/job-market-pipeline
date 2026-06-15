# Job Market Intelligence Pipeline

## Overview

Built an end-to-end data pipeline that extracts job postings from a public API, transforms nested JSON data, stores records in SQLite, and generates job market insights through SQL analytics.

## Tech Stack

- Python
- Pandas
- SQLite
- SQL
- Requests
- Git/GitHub

## Pipeline Architecture

API → Transform → SQLite Database → SQL Analytics → Intelligence Layer

## Features

- Extracts job postings from The Muse API
- Cleans nested JSON fields
- Stores structured data in SQLite
- Extracts technical skills from job descriptions
- Generates hiring trend insights
- Calculates skill concentration metrics

## Sample Insights

- Top skills by frequency
- Top hiring companies
- Skill Dominance Index (SDI)
- Company Concentration Index (CCI)

## Future Improvements

- Airflow orchestration
- AWS deployment
- Automated scheduling
- Real-time dashboard
