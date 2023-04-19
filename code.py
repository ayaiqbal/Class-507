import pandas as pd
# import necessary libraries
from sklearn.tree import DecisionTreeClassifier

# Read the dataset into a pandas dataframe
df = pd.read_csv('hospital_data.csv')

# Filter the data based on the hospital rating
filtered_df = df[df['Hospital overall rating'] >= 4]

# Print the filtered dataframe
print(filtered_df)

data = pd.read_csv('hospital_data.csv')

# define the features and target variable
X = data[['ratings', 'procedures', 'outcomes', 'other_factors']]
y = data['best_hospital']

# train the decision tree classifier
clf = DecisionTreeClassifier(random_state=0)
clf.fit(X, y)

# predict the best hospital based on input features
def predict_best_hospital(ratings, procedures, outcomes, other_factors):
    features = [[ratings, procedures, outcomes, other_factors]]
    prediction = clf.predict(features)
    return prediction[0]
