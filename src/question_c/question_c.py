#write functions here, don't add input('') statements here!
from stock import Stock

def stock_purchase_history():
    apple_stock = Stock('AAPL', 'Apple Inc')
    caterpillar_stock = Stock('CAT', 'Caterpillar')
    eastman_kodak_stock = Stock('EK', 'Eastman Kodak')
    google_stock = Stock('GOOG', 'Google')
    microsoft_stock = Stock('MSFT', 'Microsoft')

    stocks_dictionary = {
        'AAPL': apple_stock,
        'CAT': caterpillar_stock,
        'EK': eastman_kodak_stock,
        'GOOG': google_stock,
        'MSFT': microsoft_stock
    }

    print(f"{'Symbol'} {'Company Name'}")

    for stock in stocks_dictionary.values():
        print(f"{stock.get_symbol()} {stock.get_company_name()}")