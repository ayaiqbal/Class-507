# Class-507

# Project Description

This project aims to create a recommendation system for the best hospitals in the United States using a tree structure. The data for hospital performance and ratings will be obtained from various sources, including Centers for Medicare and Medicaid Services (CMS) Hospital Compare website, U.S. News & World Report Best Hospitals Rankings, Leapfrog Hospital Safety Grade, Hospital Consumer Assessment of Healthcare Providers and Systems (HCAHPS), The Joint Commission, American Hospital Association, National Quality Forum, and Healthcare Quality and Improvement.

# Required Python Packages
The following Python packages are required to run the project:

pandas: To handle data processing and manipulation.
sklearn: To build and train the decision tree model.
matplotlib: To visualize the decision tree.

# How to Run the Code
Clone the GitHub repository to your local machine.
Install the required Python packages using pip or conda package manager.
Open the main.py file, which contains the Python code for the project.
Make sure to replace the API keys or access tokens in the code, if required, for accessing the data sources.
Run the main.py file using a Python interpreter or an integrated development environment (IDE) of your choice.
The program will fetch data from the various sources, process it, build a decision tree model, and generate recommendations for the best hospitals in the US based on the tree structure.
The recommendations will be displayed on the console or visualized using matplotlib, as per the implementation.

# Data Structure 

the data is organized into a pandas DataFrame, which is a two-dimensional tabular data structure with labeled axes (rows and columns). The relevant columns from the CSV file, such as "Hospital Name", "Address", "City", "State", "ZIP Code", "County Name", "Hospital Type", "Hospital Ownership", "Emergency Services", and "Hospital overall rating", are selected using the usecols parameter in the pd.read_csv() function, and stored in the DataFrame.

The data is then sorted based on the "Hospital overall rating" column in descending order using the sort_values() function, and the top 10 hospitals are selected using the head() method. These top 10 hospitals are stored in a new DataFrame called top_10.

Next, the counts of hospitals of each type in the top 10 are calculated using the value_counts() method on the "Hospital Type" column of the top_10 DataFrame. This information is used to create a pie chart using the plt.pie() function from the matplotlib library.

Finally, the pie chart is displayed using the plt.show() function, with labels and percentages representing the distribution of hospital types among the top 10 hospitals in the US. This data organization and visualization using pandas DataFrame and matplotlib provides a convenient way to analyze and visualize the hospital data in Python.


the organization of data into data structures using the pandas library in Python. Specifically, it reads data from a CSV file (hospital_data.csv) into a pandas DataFrame, selects relevant columns using the usecols parameter, and sorts the data based on the 'Hospital overall rating' column. It then prints the top 10 hospitals based on their overall rating.

Next, it creates a pie chart using matplotlib to visualize the distribution of hospital types among the top 10 hospitals. It uses the value_counts() method to count the occurrences of each hospital type, and then creates a pie chart with the counts and labels using ax.pie() function. Finally, it adds a title to the chart using ax.set_title() method, and displays the chart using plt.show() function.

Please note that the actual organization of data into data structures may vary depending on the structure and format of the original data in the CSV file (hospital_data.csv). The code provided assumes that the data is structured with column names as keys and corresponding values as data points in a tabular format, which is commonly used in CSV files.
