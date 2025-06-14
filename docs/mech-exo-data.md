# Mech-Exo Data Pipeline

This document outlines the data ingestion and machine learning pipeline used by the Mech‑Exo service.

## Data Sources
- **Yahoo Finance** via `yfinance`
- **AlphaVantage** via REST API

Each daily run stores raw market data to the S3 bucket in the layout `raw/{symbol}/{YYYY}/{MM}/{DD}.parquet`.

## ETL
The Prefect task `calc_indicators` computes EMA(12/26), RSI(14), SMA(50/200) and a simplified Piotroski F‑Score. Results are written to `feature/{symbol}/features.parquet` for querying through Athena.

## Models
Models are trained with PyTorch Lightning using a sliding window on the feature set. Trained weights are uploaded to `models/` and can be served via TorchServe.
