import pandas as pd
from functions import *

#Read sample data
df = pd.read_csv('sample-data.csv')

# Ensure 'PricePerShare' is a float and 'CurrentHoldings' is an integer
df['PricePerShare'] = df['PricePerShare'].replace('[€\$,]', '', regex=True).astype(float)
df['CurrentHoldings'] = df['CurrentHoldings'].astype(int)

# Group by 'Date' and 'PortfolioId' for portfolio data
grouped = df.groupby(['Date', 'PortfolioId'])

# Group by 'CompanyID' for company data
company_grouped = df.groupby('CompanyID')

# Calculate the total value for each portfolio on each day
portfolio_values = grouped.apply(lambda x: (x['PricePerShare'] * x['CurrentHoldings']).sum()).reset_index(name='TotalValue')

# Example usage for posting portfolio data
for _, row in portfolio_values.iterrows():
    api_data = {
        'date': row['Date'],
        'portfolioId': row['PortfolioId'],
        'totalValue': row['TotalValue']
    }
    mock_api_call('POST', '/api/portfolio/value', api_data)

# Example usage for posting companyz data
for company_id, group in company_grouped:
    company_api_data = {
        'companyID': company_id,
        'ticker': group['Ticker'].iloc[0],  # Assuming ticker remains constant for a company
        'companyName': group['Name'].iloc[0],  # Assuming name remains constant for a company
        # Add other necessary company details here
    }
    mock_api_call('POST', '/api/companies', company_api_data)