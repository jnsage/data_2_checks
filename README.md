# data_2_checks 
Knowledge checks for Code Louisville Data Session. 

Pulls in data from [OpenBreweriesDB](https://www.openbrewerydb.org) API and converts to a pandas dataframe. Data may not be up to date, but provides good sample data for the first knowledge check.
- Displays the count of breweries listed in Kentucky.
- Displays the count of each brewery type in Kentucky.
- Uses pandasql module to query the dataframe for all brewery names listed in the City of Louisville.
- Prints the the second and third columns the dataframe.
- Prints the first 4 rows of the dataframe.

# Instructions for Check 1
From the command line:
1) Clone the [data_2_checks](https://github.com/jnsage/data_2_checks) repo from GitHub:
```
git clone git@github.com:jnsage/data_2_checks.git
```
2) Navigate to the data_2_checks directory.
3) Create and activate a virtual environment. 
4) Use pip to install system requirements:
```
pip install -r requirements.txt
```
5) Run the project:
```
python check_one.py
``` 
 