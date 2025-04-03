import pandas as pd

# Read the csv file
wards = pd.read_csv('wards.csv')

# Ensure that the data is loaded
wards.head()

# Read the csv file
census = pd.read_csv('Census.csv')

# Ensure the data is loaded
census.head()

# Apply merge (one to one)
wards_census = wards.merge(census, on='ward')

# Ensure the merge is complete
wards_census.head(4)

# Add suffixes to differentiate identical column names when they exist in both datasets.
wards_census = wards.merge(census, on='ward', suffixes=('_ward','_cen'))

# Ensure data is loaded
wards_census.head()

# Load the data
licenses = pd.read_csv('licenses.csv')

# Apply merge
ward_licenses = wards.merge(licenses, on='ward', suffixes=('_ward','_lic'))

ward_licenses.head()

# Merge movies and financials with a left join
# movies_financials = movies.merge(financials, on='id', how='left')

# Count the number of rows in the budget column that are missing
# number_of_missing_fin = movies_financials['budget'].isnull().sum()

# Load data:
# iron_1_actors = pd.read_csv('iron_1_actors')
# iron_1_actors = pd.read_csv('iron_2_actors')

# Merge iron_1_actors to iron_2_actors on id with outer join using suffixes
# iron_1_and_2 = iron_1_actors.merge(iron_2_actors, on='id', how='outer', suffixes=('_1','_2')

# Create an index that returns true if name_1 or name_2 are null
# m = ((iron_1_and_2['name_1'].isnull()) | (iron_1_and_2['name_2'].isnull()))
