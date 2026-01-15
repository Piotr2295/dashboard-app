from data.snowflake_client import fetch_incidents


def get_incident_kpis():
    df = fetch_incidents()
    return {
        "total": len(df),
        "sla_breaches": int(df["SLA_BREACHED"].sum()),
        "avg_resolution": round(df["RESOLUTION_MINUTES"].mean(), 1)
    }


def get_high_risk_incidents(threshold=0.7):
    df = fetch_incidents()
    return df[df["AI_RISK_SCORE"] > threshold]
