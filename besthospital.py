#Importing the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Selecting the relevant columns
columns = ['Hospital Name', 'Address', 'City', 'State', 'ZIP Code', 'County Name', 'Hospital Type', 'Hospital Ownership', 'Emergency Services', 'Hospital overall rating']

# Reading the data from the CSV file and selecting the relevant columns
data = pd.read_csv('hospital_data.csv', usecols=columns, encoding='latin1')

# Sorting the hospitals based on their overall rating
data_sorted = data.sort_values(by='Hospital overall rating', ascending=False)

# Printing out the top 10 hospitals
print('Top 10 hospitals in the US:')
print(data_sorted.head(10))



# Get the top 10 hospitals
top_10 = data_sorted.head(10)

# Count the number of hospitals of each type
hospital_counts = top_10['Hospital Type'].value_counts()

# Set up the figure
fig, ax = plt.subplots(figsize=(8, 6))

# Create a pie chart of the hospital types
ax.pie(hospital_counts, labels=hospital_counts.index, autopct='%1.1f%%')

# Add a title
ax.set_title('Top 10 Hospitals in the US by Type')

# Display the chart
plt.show()

