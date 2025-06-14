import pandas as pd


def calc_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate common technical indicators."""
    out = df.copy()
    close = out["close"] if "close" in out else out["Close"]
    out["ema12"] = close.ewm(span=12, adjust=False).mean()
    out["ema26"] = close.ewm(span=26, adjust=False).mean()
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    roll_up = gain.rolling(14).mean()
    roll_down = loss.rolling(14).mean()
    rs = roll_up / roll_down
    out["rsi14"] = 100 - (100 / (1 + rs))
    out["sma50"] = close.rolling(50).mean()
    out["sma200"] = close.rolling(200).mean()
    out["f_score"] = close.pct_change().rolling(9).apply(lambda x: (x > 0).sum())
    return out
