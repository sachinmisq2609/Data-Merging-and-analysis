# Data-Merging-and-analysis
This project demonstrates the use of Pandas library in Python for performing data merging and joining operations. It covers one-to-one and one-to-many merges, along with techniques for handling overlapping column names using suffixes.
# Prerequisites
You will need Python 3.6+ 
Install the Pandas library (`pip install pandas`)
Install the NumPy library (`pip install numpy`)
# Installing 
- Clone the repository first - 
- git clone https://github.com/sachinmisq2609/Data-Merging-and-analysis.git
-  Install the Pandas library: pip install pandas
The following datasets are used in this lab:
-   `wards.csv`: Contains information about Chicago wards.
-   `Census.csv`: Contains population data for Chicago wards.
-   `licenses.csv`: Contains business licenses data for Chicago wards.
# Running the tests
Below is a section explaining how to run the automated tests for this system:
1.  Execute the Python script `data_merging.py`:
- python data_merging.py
1.  Load the datasets using Pandas:
    import pandas as pd
    wards = pd.read_csv('wards.csv')
    census = pd.read_csv('Census.csv')
    licenses = pd.read_csv('licenses.csv')
2.  Perform different types of merges:
    One-to-one merge
    wards_census = wards.merge(census, on='ward', suffixes=('_ward','_cen'))
    One-to-many merge
    ward_licenses = wards.merge(licenses, on='ward', suffixes=('_ward','_lic'))
### Breakdown of Tests
-   **One-to-One Merge**: Combines `wards` and `census` datasets based on the `ward` column.
-   **One-to-Many Merge**: Combines `wards` and `licenses` datasets based on the `ward` column.
-   **Outer Join**: Demonstrates how to merge two dataframes with an outer join, handling missing values.

The test suite includes:
- Unit tests for data merging functions
- Integration tests for end-to-end workflows
- Performance tests for large datasets
- ## Deployment
This package can be imported into other Python projects or used as a standalone tool like PowerBI or Tableau. For integration with production systems, consider the following:
- Ensure all dependencies are properly managed
- Implement proper error handling for production environments
- Set up logging to monitor performance
 ## Author
Sachin Misquith - (https://github.com/sachinmisq2609)
## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
## Acknowledgments
Inspired by real-world data integration challenges
* Special thanks to Durham college and Professor Omar for their contributions
