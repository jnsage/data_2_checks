import requests
import pandas as pd
import pandasql as ps


# Read multiple API pages and create a single data_frame
page_one = requests.get('https://api.openbrewerydb.org/breweries?by_state=kentucky&per_page=50&page=1')
page_two = requests.get('https://api.openbrewerydb.org/breweries?by_state=kentucky&per_page=50&page=2')

page_one_dict = pd.read_json(page_one.text)
page_two_dict = pd.read_json(page_two.text)
df = pd.concat([page_one_dict, page_two_dict])


# Find and print TWO descriptive statistics about your data. 
num_brew = df['id'].count()
num_brewtype = df['brewery_type'].value_counts()
print(f'\nThere are {num_brew} breweries listed for Kentucky.\n')
print(f'The break down of brewery types is:\n{num_brewtype}\n')
 
# Write a query in Pandas to select a particular set of your data. Display names of breweries in city of Louisville. Locals to not overwrite df settings.
query = """ SELECT df.name FROM df WHERE df.city = 'Louisville' """
results = ps.sqldf(query, locals())
print(f'The following breweries are in Louisville:\n{results}\n')

# Select and print the SECOND AND THIRD columns of your data frame.
columns = df.iloc[:,[1,2]]
print(f'Second and third Columns:\n{columns}\n')

# Select and print the FIRST 4 rows of you data frame.
rows = df.iloc[0:4]
print(f'First 4 rows:\n{rows}')