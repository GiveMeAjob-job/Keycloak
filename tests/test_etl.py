import pandas as pd
import sys
sys.path.insert(0, 'python')
from mech_exo.etl.indicators import calc_indicators


def test_calc_indicators():
    df = pd.DataFrame({"close": [1,2,3,4,5,6,7,8,9,10]})
    out = calc_indicators(df)
    assert "ema12" in out.columns
    assert "rsi14" in out.columns
