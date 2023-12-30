from utils.create_date_table import create_date_table
from utils.extract_fred_data import extract_fred_data

def capture_multiple_fred_series(fred_series_to_capture, fred_api_key):
    """This function returns a dataframe containing all the values returned from FRED tied to a master calendar. 

    Args:
        fred_series_to_capture (list): A list of FRED series values that should be returned from FRED.
        fred_api_key (string): An account's FRED API key

    Returns:
        DataFrame: This dataframe contains all of the FRED series values along with a master calendar. 
    """

    master_calendar = create_date_table()

    for fred_series in fred_series_to_capture:

        months = None
        data = None

        data, months = extract_fred_data(
            fred_api_key=fred_api_key, fred_series=fred_series)

        master_calendar = master_calendar.merge(data, on='date', how='left')

        master_calendar[str.lower(fred_series)] = master_calendar[str.lower(fred_series)].ffill()

    return master_calendar