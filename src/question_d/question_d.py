#write functions here, don't add input('') statements here!
from Stock import Stock

def single_stock():
    apple_stock = Stock('AAPL', 'Apple Inc')

    print("Stock Report")
    print("Company Symbol")
    print(f"{apple_stock.get_company_name()} {apple_stock.get_symbol()}")