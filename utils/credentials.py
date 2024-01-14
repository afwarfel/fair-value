from os.path import exists
import pandas as pd
import collections
import os


def credentials():
    """
    Check if a credentials file already exists and if it doesn't, generate one and ask the user for all of their credentials which will then be stored. This should make the process more streamlined and not require any credentials to be committed to a repo.
    """

    # Here you define all of the credentials that you'll need from the user
    required_credentials = ["FRED API Key", "AlphaVantage API Key"]

    credentials_pathway = os.path.join(
        os.path.dirname(__file__), "..", "data", "credentials.json"
    )

    if exists(credentials_pathway):
        credentials = pd.read_json(credentials_pathway, orient="records")
    else:
        credentials = {}
        for required_credential in required_credentials:
            credentials[required_credential] = input(
                "What is your "
                + required_credential
                + "? (Note: If you are unsure, leave blank as it may not be a credential you need to run this script)"
            )
        pd.DataFrame(credentials, index=[0]).to_json(
            credentials_pathway, orient="records", indent=4
        )
        print("Credentials stored within data folder...")

    credentials = pd.read_json(credentials_pathway)
    if collections.Counter(required_credentials) != collections.Counter(
        credentials.columns
    ):
        for required_credential in required_credentials:
            if required_credential not in credentials.columns:
                credentials[required_credential] = input(
                    "What is your " + required_credential + "? "
                )
        pd.DataFrame(credentials, index=[0]).to_json(
            credentials_pathway, orient="records", indent=4
        )
        print("Updating credentials stored within data folder...")

    for x in required_credentials:
        if len(credentials[x][0]) == 0:
            credentials[x] = input("What is your " + x + "? ")
            pd.DataFrame(credentials, index=[0]).to_json(
                credentials_pathway, orient="records", indent=4
            )
            print("Updating credentials stored within data folder...")

    # Create a dictionary where the name of the credential is the key and the value is the value of the credential
    credentials = credentials.to_dict(orient="records")[0]

    return credentials
