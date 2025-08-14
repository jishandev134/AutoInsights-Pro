import pandas as pd

def clean_and_summarize(file):
    """
    Reads the uploaded CSV, cleans it, and returns:
    - cleaned DataFrame
    - summary statistics
    """

    # Read CSV into DataFrame
    df = pd.read_csv(file)

    # Basic cleaning: remove duplicates & handle missing values
    df.drop_duplicates(inplace=True)
    df.fillna("N/A", inplace=True)

    # Summary statistics
    summary = df.describe(include="all").transpose()

    return df, summary
