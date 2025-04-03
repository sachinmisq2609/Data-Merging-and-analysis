import pandas as pd

def perform_data_merging():
    """
    Demonstrates data merging operations using Pandas.
    """
    # Load datasets
    try:
        wards = pd.read_csv('wards.csv')
        census = pd.read_csv('Census.csv')
        licenses = pd.read_csv('licenses.csv')
    except FileNotFoundError as e:
        print(f"Error loading data files: {e}")
        return

    # One-to-one merge
    try:
        wards_census = wards.merge(census, on='ward')
        print("One-to-One Merge (wards and census):")
        print(wards_census.head())
    except Exception as e:
        print(f"Error performing one-to-one merge: {e}")

    # One-to-many merge
    try:
        ward_licenses = wards.merge(licenses, on='ward', suffixes=('_ward', '_lic'))
        print("\nOne-to-Many Merge (wards and licenses):")
        print(ward_licenses.head())
    except Exception as e:
        print(f"Error performing one-to-many merge: {e}")

if __name__ == "__main__":
    perform_data_merging()
