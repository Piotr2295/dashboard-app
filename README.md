# AI Operations Dashboard

A lightweight Streamlit application demonstrating how AI-driven operational insights can be surfaced to operators using Snowflake as an analytics backend.

## Tech Stack
- Python
- Snowflake
- Streamlit
- Pandas

## Features
- Incident analytics from Snowflake
- SLA breach tracking
- AI risk score visualization
- Operator-friendly dashboard

## Architecture
Snowflake → Python Services → Streamlit UI

## How to Run
1. Create Snowflake database and table (see SQL in `/sql`)
2. Set environment variables
3. Install dependencies:
   pip install -r requirements.txt
4. Run:
   streamlit run app.py
