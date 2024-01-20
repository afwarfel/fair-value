import pandas as pd
import os


def extract_r_star_data():
    """Extracts r_star data from the New York Fed website and saves it as a csv file in the data folder."""
    link_for_r_star_estimates = "https://www.newyorkfed.org/medialibrary/media/research/economists/williams/data/Holston_Laubach_Williams_current_estimates.xlsx"
    r_star_estimates = pd.read_excel(
        link_for_r_star_estimates, sheet_name="HLW Estimates", skiprows=4, index_col=0
    )

    r_star_estimates = r_star_estimates.dropna(axis=1, how="all")
    cols = r_star_estimates.columns.tolist()

    for i in range(1, len(cols)):
        if "Unnamed" in cols[i]:
            cols[i] = cols[i - 1]

    r_star_estimates.columns = cols

    r_star_estimates.columns = (
        r_star_estimates.columns + " " + r_star_estimates.iloc[0].astype(str)
    )

    r_star_estimates = r_star_estimates.drop(r_star_estimates.index[0])
    r_star_estimates.columns = r_star_estimates.columns.str.lower().str.replace(
        " ", "_"
    )
    r_star_estimates.columns = r_star_estimates.columns.str.replace("*", "_star")
    r_star_estimates.columns = r_star_estimates.columns.str.replace(
        "[(),]", "", regex=True
    )

    r_star_estimates.index.name = "date"
    r_star_estimates.index = pd.to_datetime(r_star_estimates.index)
    try:
        r_star_estimates.to_csv(os.path.join("..", "data", "r_star_estimates.csv"))
    except:
        r_star_estimates.to_csv(os.path.join("data", "r_star_estimates.csv"))


if __name__ == "__main__":
    extract_r_star_data()
