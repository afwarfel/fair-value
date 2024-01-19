from utils.credentials import credentials
import pandas as pd
from dotenv import load_dotenv
import requests, os

load_dotenv()  # take environment variables from .env.
alpha_vantage_api_key = os.getenv("alpha_vantage_api_key")


def pull_data_from_alphavantage(ticker, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={api_key}&datatype=csv&outputsize=full"
    df = pd.read_csv(url)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df.set_index("timestamp", inplace=True)
    df = df.resample("D").asfreq()
    df = df.fillna(method="ffill")
    return df


sector_etfs = [
    "XLC",
    "XLY",
    "XLP",
    "XLE",
    "XLF",
    "XLV",
    "XLI",
    "XLB",
    "XLRE",
    "XLK",
    "XLU",
    "SPY",
]

dfs = []

for sector in sector_etfs:
    df = pull_data_from_alphavantage(sector, alpha_vantage_api_key)
    df["Ticker"] = sector
    dfs.append(df)


final_df = pd.concat(dfs)
final_df.to_csv(os.path.join("data", "sector_etfs.csv"), index=True)
