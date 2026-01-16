from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.incident_service import (
    get_incident_kpis,
    get_high_risk_incidents
)
from data.snowflake_client import fetch_incidents

app = FastAPI(
    title="Ops Dashboard API",
    description="API exposing AI-driven operational insights",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/incidents")
def get_incidents():
    df = fetch_incidents()
    return df.to_dict(orient="records")

@app.get("/incidents/high-risk")
def high_risk(threshold: float = 0.7):
    df = get_high_risk_incidents(threshold)
    return df.to_dict(orient="records")

@app.get("/incidents/kpis")
def kpis():
    return get_incident_kpis()
