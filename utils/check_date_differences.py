import numpy as np
import pandas as pd

def check_date_differences(df):
    """FRED returns data with a date column and the value column. The date column contains the start date for the period in question. This creates a problem because FRED makes it seem as if the value is known as of the date in the date column. This means we need to push the date columns forward by the frequency of the time series so that the value is tied to the date when the period ends. For example, Q2 values come from FRED tied to 4/1 which doesn't make much sense because those values aren't known as of 4/1. In this example, the series is quarterly, so we push those values to 6/30 so that the values are more closely tied to the date on which they are known.

    Args:
        df (DataFrame): This is a dataframe from FRED containing a date column and then a value column with the time series.

    Returns:
        DataFrame: A dataframe of the same dimensions with dates pushed forward by the length of one period. 
    """

    most_recent_date = df['date'].values[-1]
    second_most_recent_date = df['date'].values[-2]

    months = int(round(
        (((most_recent_date - second_most_recent_date)/np.timedelta64(1, 'D')))/30, 0))

    df['date'] = df['date'] + pd.DateOffset(months=months)

    return df, months