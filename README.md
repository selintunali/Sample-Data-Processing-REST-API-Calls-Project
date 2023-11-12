# Script for Parsing and API Call Generation

## Introduction
This script is designed to parse financial data from a CSV file, calculate the total value of different portfolios, and generate mock API calls for posting portfolio and company data into a mock system. It's intended to automate and streamline the process of data management for financial portfolios.

## Design Overview
The script is structured to:

- Read data from a CSV file.
- Clean and process the data, focusing on price per share and current holdings.
- Group the data by portfolio and company.
- Calculate the total value of each portfolio.
- Generate mock API calls to post this data.

## Dependencies
- Pandas: Used for data manipulation and analysis.

## How to Run the Script
To run the script, ensure that you have Python installed on your system along with the Pandas library. Place the script and the CSV file in the same directory. Run the script using a Python interpreter.

```
python script_name.py
```

## Data Processing
The script reads data from 'sample-data.csv', focusing on columns such as 'CompanyID', 'PortfolioId', 'PricePerShare', and 'CurrentHoldings'. It cleans the 'PricePerShare' data by removing currency symbols and converting the values to floats for numerical computation.

## Calculations and Groupings
Data is grouped by both 'Date' and 'PortfolioId' for portfolio calculations, and by 'CompanyID' for company data. The script calculates the total value of holdings for each portfolio by multiplying 'PricePerShare' by 'CurrentHoldings' and summing these values.

## Mock API Calls
Mock API calls are generated to demonstrate how the script would interact with an API endpoint. For portfolios, the API call posts the calculated total value of each portfolio. For companies, it posts company-specific data.

## Parameters and Variables
Key parameters include:

- Date: The date of the record.
- PortfolioId: Identifier for the portfolio.
- CompanyID: Identifier for the company.
- Other data fields such as 'PricePerShare' and 'CurrentHoldings'.

## Error Handling and Limitations
The script includes basic error handling for data type conversion and missing values. However, it assumes well-formatted and complete input data. Any inconsistencies in the CSV format may require additional handling.

## Future Enhancements
Future enhancements could include:

- Integration with a real API for live data processing.
- Advanced error handling and data validation.
- User interface for file selection and parameter input.

## Sample Output
```
POST Request to /api/portfolio/value: {'date': '1/1/23', 'portfolioId': 120, 'totalValue': 2430000.0}
POST Request to /api/portfolio/value: {'date': '1/1/23', 'portfolioId': 235, 'totalValue': 1040000.0}
POST Request to /api/portfolio/value: {'date': '1/1/23', 'portfolioId': 340, 'totalValue': 8689182.02}
POST Request to /api/portfolio/value: {'date': '1/10/23', 'portfolioId': 120, 'totalValue': 6012250.0}
POST Request to /api/portfolio/value: {'date': '1/10/23', 'portfolioId': 235, 'totalValue': 1030000.0}
POST Request to /api/portfolio/value: {'date': '1/10/23', 'portfolioId': 340, 'totalValue': 8501000.0}
POST Request to /api/portfolio/value: {'date': '1/2/23', 'portfolioId': 120, 'totalValue': 4868000.0}
POST Request to /api/portfolio/value: {'date': '1/2/23', 'portfolioId': 235, 'totalValue': 1133000.0}
POST Request to /api/portfolio/value: {'date': '1/2/23', 'portfolioId': 340, 'totalValue': 8224983.36}
POST Request to /api/portfolio/value: {'date': '1/3/23', 'portfolioId': 120, 'totalValue': 4936912.0}
POST Request to /api/portfolio/value: {'date': '1/3/23', 'portfolioId': 235, 'totalValue': 1302000.0}
POST Request to /api/portfolio/value: {'date': '1/3/23', 'portfolioId': 340, 'totalValue': 9176785.44}
POST Request to /api/portfolio/value: {'date': '1/4/23', 'portfolioId': 120, 'totalValue': 4865418.0}
POST Request to /api/portfolio/value: {'date': '1/4/23', 'portfolioId': 235, 'totalValue': 1283000.0}
POST Request to /api/portfolio/value: {'date': '1/4/23', 'portfolioId': 340, 'totalValue': 6568174.399999999}
POST Request to /api/portfolio/value: {'date': '1/5/23', 'portfolioId': 120, 'totalValue': 4581295.0}
POST Request to /api/portfolio/value: {'date': '1/5/23', 'portfolioId': 235, 'totalValue': 1156560.0}
POST Request to /api/portfolio/value: {'date': '1/5/23', 'portfolioId': 340, 'totalValue': 7206913.600000001}
POST Request to /api/portfolio/value: {'date': '1/6/23', 'portfolioId': 120, 'totalValue': 4430710.0}
POST Request to /api/portfolio/value: {'date': '1/6/23', 'portfolioId': 235, 'totalValue': 1184090.0}
POST Request to /api/portfolio/value: {'date': '1/6/23', 'portfolioId': 340, 'totalValue': 10464000.0}
POST Request to /api/portfolio/value: {'date': '1/7/23', 'portfolioId': 120, 'totalValue': 4815720.0}
POST Request to /api/portfolio/value: {'date': '1/7/23', 'portfolioId': 235, 'totalValue': 1251000.0}
POST Request to /api/portfolio/value: {'date': '1/7/23', 'portfolioId': 340, 'totalValue': 8832000.0}
POST Request to /api/portfolio/value: {'date': '1/8/23', 'portfolioId': 120, 'totalValue': 3633000.0}
POST Request to /api/portfolio/value: {'date': '1/8/23', 'portfolioId': 235, 'totalValue': 1246500.0}
POST Request to /api/portfolio/value: {'date': '1/8/23', 'portfolioId': 340, 'totalValue': 8456500.0}
POST Request to /api/portfolio/value: {'date': '1/9/23', 'portfolioId': 120, 'totalValue': 4354000.0}
POST Request to /api/portfolio/value: {'date': '1/9/23', 'portfolioId': 235, 'totalValue': 1240000.0}
POST Request to /api/portfolio/value: {'date': '1/9/23', 'portfolioId': 340, 'totalValue': 9146500.0}
POST Request to /api/companies: {'companyID': 111230, 'ticker': 'AAPL US', 'companyName': 'Apple Inc.'}
POST Request to /api/companies: {'companyID': 111232, 'ticker': 'JNJ US', 'companyName': 'Johnson and Johnson'}
POST Request to /api/companies: {'companyID': 111236, 'ticker': 'BA US', 'companyName': 'Boeing Co'}
POST Request to /api/companies: {'companyID': 111240, 'ticker': 'GOOGL', 'companyName': 'Alphabet Inc'}
POST Request to /api/companies: {'companyID': 111242, 'ticker': 'NVDA US', 'companyName': 'Nvidia Corp'}
POST Request to /api/companies: {'companyID': 211250, 'ticker': 'VALE', 'companyName': 'Vale SA'}
POST Request to /api/companies: {'companyID': 211546, 'ticker': 'SGML', 'companyName': 'Sigma Lithium Corp'}
POST Request to /api/companies: {'companyID': 231214, 'ticker': 'BABA', 'companyName': 'Alibaba Group Holding Ltd'}
```