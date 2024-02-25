import matplotlib.pyplot as plt

# Read data from the SQLite database
financial_data = pd.read_sql('SELECT * FROM financial_data', con=your_sqlalchemy_engine)

# Plotting spending and profits over the years
plt.plot(financial_data['Year'], financial_data['Spending'], label='Spending')
plt.plot(financial_data['Year'], financial_data['Profits'], label='Profits')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.legend()
plt.show()
