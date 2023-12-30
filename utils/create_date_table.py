import pandas as pd

def create_date_table(start='1900-01-01', end=pd.Timestamp.today()):
    """This function is meant to create a master date table starting from a start date to an end date with many other columns attached to it that identify quarters, weeks, etc. 

    Args:
        start (str, optional): The start date for your master date table. Defaults to '1900-01-01'.
        end (DateTime, optional): The end date for your master date table. Defaults to pd.Timestamp.today().

    Returns:
        DataFrame: This is a dataframe containing one record for each day between the start and the end date.
    """

    df = pd.DataFrame({"date": pd.date_range(start, end)})

    # Set index as date
    df = df.set_index('date')

    # Raise a value error if the index is duplicated
    if df.index.duplicated().any():
        raise ValueError('Index is duplicated')

    return df