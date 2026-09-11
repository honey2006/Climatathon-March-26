def get_latest_entry(csvFile):
    import pandas as pd

    data = pd.read_csv(csvFile)

    # Get latest row
    latest_entry = data.iloc[-1]

    return latest_entry