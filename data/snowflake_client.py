import snowflake.connector
import pandas as pd
import numpy as np
from config.snowflake_config import SNOWFLAKE_CONFIG


def get_connection():
    return snowflake.connector.connect(**SNOWFLAKE_CONFIG)


def fetch_incidents():
    conn = get_connection()
    query = "SELECT * FROM incidents"
    df = pd.read_sql(query, conn)
    df = df.replace({np.nan: None})
    conn.close()
    return df
