'''
This file is used to run the main program.
'''

import gspread
from google.oauth2.service_account import Credentials

# Define the scope

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

sales = SHEET.worksheet('sales')

sales_data = sales.get_all_values()

print(sales_data)

surplus = SHEET.worksheet('surplus')

surplus_data = surplus.get_all_values()

print(surplus_data)

stock = SHEET.worksheet('stock')

stock_data = stock.get_all_values()

print(stock_data)