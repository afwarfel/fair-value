from fredapi import Fred
import pandas as pd
from utils.check_date_differences import check_date_differences


def extract_fred_data(fred_api_key, fred_series):
    """This function returns FRED data as a time series with dates for the latest value as it's known.

    Args:
        fred_api_key (string): An account's FRED API key
        fred_series (string): The FRED series to capture

    Returns:
        dataframe, int: The first return is a dataframe of the FRED series, the second return is the number of months between observations.
    """
    fred = Fred(api_key=fred_api_key)
    data = fred.get_series(fred_series).to_frame().reset_index()
    data = data.set_axis(["date", str.lower(fred_series)], axis=1)
    data, months = check_date_differences(data)
    data = data.set_index("date")
    data.index = pd.to_datetime(data.index)

    return data, months
