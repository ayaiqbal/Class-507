# Importing the necessary libraries
import pandas as pd

# Selecting the relevant columns
columns = ['Hospital Name', 'Address', 'City', 'State', 'ZIP Code', 'County Name', 'Hospital Type', 'Hospital Ownership', 'Emergency Services', 'Hospital overall rating']

# Reading the data from the CSV file and selecting the relevant columns
data = pd.read_csv('hospital_data.csv', usecols=columns, encoding='latin1')

# Sorting the hospitals based on their overall rating
data_sorted = data.sort_values(by='Hospital overall rating', ascending=False)

# Printing out the top 10 hospitals
print('Top 10 hospitals in the US:')
print(data_sorted.head(10))
