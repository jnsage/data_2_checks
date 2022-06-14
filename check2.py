# Show number of rows is less after dropping NaN in titles
import urllib
import pandas as pd

workbook = '1zYw_XAiYyBTjJOrxXZyetcQC-grdXO5D4CVt2zRIhBc'
sheet_name = 'Check2'
url = f'https://docs.google.com/spreadsheets/d/{workbook}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

# Import Google Sheet as a DataFrame. Replace any string values in the 'Date' and 'Time' columns with a datetime objects.
try:
    movie_df = pd.read_csv(url, parse_dates=['Date','Time'])
except urllib.error.URLError:
    print("There is no internet connection. Please connect to the internet and try again.")

    # Correct title spelling. Weekday > Day_of_week, time > showtime
print('Original column names: ', movie_df.columns)

renamed_columns = {'Year' : 'Year',
                 'ttle' : 'Title',
                 'Theater' : 'Theater',
                 'Weekday' : 'Day',
                 'Date' : ' Date',
                 'Time' : ' Showtime',
                 'Saw with April' : 'With April'
}
movie_df.rename(columns=renamed_columns, inplace=True)

print('New column names: ', movie_csv.columns)

#Drop rows with NaN in Title column

# Drop rows with NaN in Title column

print('Original dataframe shape: ', movie_df.shape)
movie_df.dropna(subset=['Title'], inplace=True)

# Show number of rows is less after dropping NaN in titles
print('New dataframe shape: ', movie_df.shape)

# Check value names in the theater column
movie_df['Theater'].unique()

# Replace 2 names and display new values to check changes
movie_df['Theater'].replace(to_replace={'Village Eight' : 'Village 8' , 'Ft. Lauderdale EcoDiscovery Center IMAX' : 'Ft. Lauderdale Eco Discovery Center'}, inplace=True)
movie_df['Theater'].unique()

# Fill in missing years. Show if any values in the series are NaN and look at first 5 rows to validate. 
print('NaN Exists: ', movie_df['Year'].isnull().values.any())
print(movie_df['Year'].head())

# Fill in year with year copied from date column
movie_df['Year'] = movie_df['Date'].dt.year

# Show if any values in the series are NaN and look at first 5 rows to validate. 
print('NaN Exists: ', movie_df['Year'].isnull().values.any())
print(movie_df['Year'].head())

# Check to see if any more NaN exists in entire dataframe. Print to validate column changes, 
print('NaN Exists in movie_df: ', movie_df.isnull().values.any())
movie_df