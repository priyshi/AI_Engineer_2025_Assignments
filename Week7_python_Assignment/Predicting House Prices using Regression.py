import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

house_data = pd.read_csv('house_price_regression_dataset.csv')
print(house_data.head())


# Check for missing values
print("\nMissing values per column:")
print(house_data.isnull().sum())
print(house_data.isna().sum())

# Scatter plot using matplotlib
plt.figure(figsize=(8, 5))
plt.scatter(house_data['Square_Footage'], house_data['House_Price'], alpha=0.6)

plt.title('Relationship between Square Footage and Price')
plt.xlabel('Square_Footage')
plt.ylabel('House_Price')
plt.grid(True)
plt.show()

# Scatter plot using seaborn
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Square_Footage', y='House_Price', data=house_data)
plt.title('Relationship between Square Footage and Price') 
plt.xlabel('Square_Footage')
plt.ylabel('House_Price')
plt.show()

x = house_data[['Square_Footage']] # independent variable (feature)']]   
y = house_data['House_Price']  # dependent variable (target)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#5. Model Building
#Create a Linear Regression model using LinearRegression from sklearn.linear_model.
# Fit the model on the training data.
# Display the intercept (b₀) and coefficient (b₁) of the regression line

linear = LinearRegression()
linear.fit(X_train, y_train)
print(f"Intercept (b₀): {linear.intercept_}")
print(f"Coefficient (b₁): {linear.coef_[0]}")

# Prediction and Evaluation
# o Predict the house prices for the test set.
# o Calculate and print the following evaluation metrics:
#  Mean Squared Error (MSE)
#  Root Mean Squared Error (RMSE)
#  R² Score (Coefficient of Determination)

y_predict = linear.predict(X_test)
print(f"Mean Squared Error (MSE): {mean_squared_error(y_test, y_predict)}")
print(f"Root Mean Squared Error (RMSE): {np.sqrt(mean_squared_error(y_test, y_predict))}")
print(f"R² Score: {r2_score(y_test, y_predict)}")

# Visualization
# o Plot the regression line along with the actual data points.
# o Visualize actual vs predicted prices to assess model performance


plt.scatter(X_test, y_test, color='blue', label='Actual Prices')
plt.plot(X_test, y_predict, color='red', linewidth=2, label='Predicted Prices')
plt.xlabel('Square Footage')
plt.ylabel('House Price')
plt.title('Square Footage vs House Price')
plt.legend()
plt.show()

# run time prediction

try:
    sqft = float(input("Enter the Square Footage of the house: "))
    #predicted_price = linear.predict([[sqft]])
    predicted_price = pd.DataFrame([[sqft]], columns=X_train.columns)
    Final_predicted_price=linear.predict(predicted_price)
    print(f"\nPredicted House Price for {sqft} sq.ft is ₹{Final_predicted_price[0]:,.2f}")
except ValueError:
    print("⚠️ Please enter a valid number for square footage.")
