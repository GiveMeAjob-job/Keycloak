import io
from datetime import datetime
from typing import Optional

import pandas as pd
import requests
import boto3

BASE_URL = "https://www.alphavantage.co/query"


def fetch_daily(symbol: str, api_key: str, output_size: str = "compact") -> pd.DataFrame:
    """Fetch daily adjusted data from AlphaVantage."""
    params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": symbol,
        "outputsize": output_size,
        "apikey": api_key,
    }
    resp = requests.get(BASE_URL, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json().get("Time Series (Daily)", {})
    df = pd.DataFrame.from_dict(data, orient="index").sort_index()
    df.index = pd.to_datetime(df.index)
    df = df.rename(columns=lambda c: c.split(". ")[1])
    for col in df.columns:
        df[col] = pd.to_numeric(df[col])
    return df


def save_to_s3(df: pd.DataFrame, bucket: str, symbol: str, date: datetime) -> str:
    key = f"raw/{symbol}/{date:%Y}/{date:%m}/{date:%d}.parquet"
    buffer = io.BytesIO()
    df.to_parquet(buffer)
    buffer.seek(0)
    boto3.client("s3").upload_fileobj(buffer, bucket, key)
    return key
