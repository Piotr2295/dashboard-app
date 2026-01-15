import snowflake.connector
import pandas as pd
from config.snowflake_config import SNOWFLAKE_CONFIG


def get_connection():
    return snowflake.connector.connect(**SNOWFLAKE_CONFIG)


def fetch_incidents():
    conn = get_connection()
    query = "SELECT * FROM incidents"
    df = pd.read_sql(query, conn)
    conn.close()
    return df
