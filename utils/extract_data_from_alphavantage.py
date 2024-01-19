import pandas as pd
from dotenv import load_dotenv
import requests, os


def extract_data_from_alphavantage(ticker, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={api_key}&datatype=csv&outputsize=full"
    df = pd.read_csv(url)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df.set_index("timestamp", inplace=True)
    df = df.resample("D").asfreq()
    df = df.ffill()
    return df


def extract_sector_etf_data_from_alphavantage():
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

    load_dotenv()  # take environment variables from .env.
    alphavantage_api_key = os.getenv("alphavantage_api_key")

    dfs = []

    for sector in sector_etfs:
        df = extract_data_from_alphavantage(sector, alphavantage_api_key)
        df["Ticker"] = sector
        dfs.append(df)

    final_df = pd.concat(dfs)
    final_df.to_csv(os.path.join("data", "sector_etfs.csv"), index=True)


if __name__ == "__main__":
    extract_sector_etf_data_from_alphavantage()
