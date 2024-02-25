import pandas as pd

# Assuming you have a method to get data from SAP S/4
sap_data = get_sap_data()

# Assuming the data is in a DataFrame format, modify this based on the actual SAP S/4 data structure
financial_data = sap_data[['Year', 'Spending', 'Profits']]

# Save data to an SQLite database
financial_data.to_sql('financial_data', con=your_sqlalchemy_engine, index=False, if_exists='replace')
