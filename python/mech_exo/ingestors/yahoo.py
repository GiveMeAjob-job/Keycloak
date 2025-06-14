import io
from datetime import datetime
from typing import Optional

import yfinance as yf
import pandas as pd
import boto3


def fetch(symbol: str, start: Optional[str] = None, end: Optional[str] = None, interval: str = "1d") -> pd.DataFrame:
    """Fetch historical price data from Yahoo Finance."""
    return yf.download(symbol, start=start, end=end, interval=interval)


def save_to_s3(df: pd.DataFrame, bucket: str, symbol: str, date: datetime) -> str:
    """Save dataframe to S3 in the raw bucket layout."""
    key = f"raw/{symbol}/{date:%Y}/{date:%m}/{date:%d}.parquet"
    buffer = io.BytesIO()
    df.to_parquet(buffer)
    buffer.seek(0)
    s3 = boto3.client("s3")
    s3.upload_fileobj(buffer, bucket, key)
    return key
