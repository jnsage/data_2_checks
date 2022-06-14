# data_2_checks 
Knowledge checks for Code Louisville Data Session. 

## Knowledge Check 1
Pulls in data from [OpenBreweriesDB](https://www.openbrewerydb.org) API and converts to a pandas dataframe. Data may not be up to date, but provides good sample data for the first knowledge check.
- Displays the count of breweries listed in Kentucky.
- Displays the count of each brewery type in Kentucky.
- Uses pandasql module to query the dataframe for all brewery names listed in the City of Louisville.
- Prints the the second and third columns the dataframe.
- Prints the first 4 rows of the dataframe.

## Instructions for Check 1
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

## Knowledge Check 2
 Pulls in data from [TicketStubsDigital](https://docs.google.com/spreadsheets/d/1zYw_XAiYyBTjJOrxXZyetcQC-grdXO5D4CVt2zRIhBc) Google Sheet and converts to a pandas dataframe. Then goes does the following data cleaning:

 1) Rename column headers.
 2) Drop rows where the movie title is missing
 3) Replace misspelled values in the Theater column
 4) Fill in missing values in the Year column

 ## Instructions for Check 2
 From the command line:
1) Clone the [data_2_checks](https://github.com/jnsage/data_2_checks) repo from GitHub: 

2) Navigate to the data_2_checks directory.
3) Create and activate a virtual environment. 
4) Use pip to install system requirements:
```
pip install -r requirements.txt
```
5) Run jupyter notebook:
```
jupyter notebook
``` 
6) The Jupyter Notebook will open in a web browser. Click on "check2.ipynb" to run the notebook.

7) Run code cells one at a time to alter the dataframe.

