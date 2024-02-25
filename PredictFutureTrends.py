from sklearn.linear_model import LinearRegression
import numpy as np

# Assuming a simple linear regression model for prediction
X = np.array(financial_data['Year']).reshape(-1, 1)
y_spending = np.array(financial_data['Spending'])
y_profits = np.array(financial_data['Profits'])

model_spending = LinearRegression().fit(X, y_spending)
model_profits = LinearRegression().fit(X, y_profits)

# Predict future trends
future_years = np.array([2025, 2026, 2027]).reshape(-1, 1)
predicted_spending = model_spending.predict(future_years)
predicted_profits = model_profits.predict(future_years)

# Plotting the predictions
plt.plot(financial_data['Year'], financial_data['Spending'], label='Spending')
plt.plot(financial_data['Year'], financial_data['Profits'], label='Profits')
plt.plot(future_years, predicted_spending, 'o--', label='Predicted Spending')
plt.plot(future_years, predicted_profits, 'o--', label='Predicted Profits')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.legend()
plt.show()
