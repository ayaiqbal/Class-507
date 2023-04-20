import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

# Selecting the relevant columns
columns = ['Hospital Name', 'Address', 'City', 'State', 'ZIP Code', 'County Name', 'Hospital Type', 'Hospital Ownership', 'Emergency Services', 'Hospital overall rating']

# Reading the data from the CSV file and selecting the relevant columns
data = pd.read_csv('hospital_data.csv', usecols=columns, encoding='latin1')

# Encode categorical columns
data = pd.get_dummies(data, columns=['Hospital Type', 'Hospital Ownership', 'Emergency Services'])

# Splitting the data into training and testing sets
X = data.drop(['Hospital Name', 'Address', 'City', 'State', 'ZIP Code', 'County Name', 'Hospital overall rating'], axis=1)
y = data['Hospital overall rating']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and training the decision tree model
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)

# ...

# Evaluating the model on the test set
score = model.score(X_test, y_test)
print('Model accuracy:', score)

# Extracting the most important features
feature_importances = model.feature_importances_
features = list(X.columns)
importances = dict(zip(features, feature_importances))

# Sorting the features by importance
sorted_importances = sorted(importances.items(), key=lambda x: x[1], reverse=True)

# Printing out the top 5 most important features
print('Top 5 most important features for predicting hospital quality ratings:')
for feature, importance in sorted_importances[:5]:
    print(f'{feature}: {importance}')


# Plotting a bar chart of the top 5 most important features
plt.bar([x[0] for x in sorted_importances[:5]], [x[1] for x in sorted_importances[:5]])
plt.xticks(rotation=90)
plt.ylabel('Feature Importance')
plt.title('Top 5 most important features for predicting hospital quality ratings')
plt.show()    

# Predicting hospital quality ratings for the top 10 hospitals
top_hospitals = data.sort_values(by='Hospital overall rating', ascending=False).head(10)
X_top = top_hospitals.drop(['Hospital Name', 'Address', 'City', 'State', 'ZIP Code', 'County Name', 'Hospital overall rating'], axis=1)
y_pred = model.predict(X_top)
print('Predicted hospital quality ratings for the top 10 hospitals:')
print(y_pred)

# Plotting a pie chart of the predicted hospital quality ratings
plt.pie(y_pred, labels=top_hospitals['Hospital Name'], autopct='%1.1f%%')
plt.title('Predicted hospital quality ratings for the top 10 hospitals')
plt.show()


