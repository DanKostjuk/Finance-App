import pandas as pd
import yfinance as yf
import json
# library by ranaroussi

def pr(d):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(d)


stocks = {
    "apple inc.": "AAPL",
    "apple": "AAPL",
    "AAPL": "AAPL",
    "microsoft corporation": "MSFT",
    "microsoft": "MSFT",
    "MSFT": "MSFT",
    "amazon.com inc.": "AMZN",
    "amazon": "AMZN",
    "AMZN": "AMZN",
    "alphabet inc.": "GOOGL",
    "google": "GOOGL",
    "GOOGL": "GOOGL",
    "meta platforms, inc. (facebook)": "META",
    "facebook": "META",
    "meta": "META",
    "META": "META",
    "tesla, inc.": "TSLA",
    "tesla": "TSLA",
    "TSLA": "TSLA",
    "nvidia corporation": "NVDA",
    "nvidia": "NVDA",
    "NVDA": "NVDA",
    "berkshire hathaway inc. (class a)": "BRK.A",
    "berkshire hathaway a": "BRK.A",
    "BRK.A": "BRK.A",
    "berkshire hathaway inc. (class b)": "BRK.B",
    "berkshire hathaway b": "BRK.B",
    "BRK.B": "BRK.B",
    "jpmorgan chase & co.": "JPM",
    "jpmorgan": "JPM",
    "JPM": "JPM",
    "johnson & johnson": "JNJ",
    "johnson": "JNJ",
    "j&j": "JNJ",
    "JNJ": "JNJ",
    "visa inc.": "V",
    "visa": "V",
    "V": "V",
    "procter & gamble co.": "PG",
    "procter & gamble": "PG",
    "p&g": "PG",
    "PG": "PG",
    "unitedhealth group incorporated": "UNH",
    "unitedhealth": "UNH",
    "UNH": "UNH",
    "home depot, inc.": "HD",
    "home depot": "HD",
    "HD": "HD",
    "mastercard incorporated": "MA",
    "mastercard": "MA",
    "MA": "MA",
    "verizon communications inc.": "VZ",
    "verizon": "VZ",
    "VZ": "VZ",
    "pfizer inc.": "PFE",
    "pfizer": "PFE",
    "PFE": "PFE",
    "coca-cola company": "KO",
    "coca-cola": "KO",
    "coke": "KO",
    "KO": "KO",
    "walt disney company": "DIS",
    "disney": "DIS",
    "DIS": "DIS",
    "intel corporation": "INTC",
    "intel": "INTC",
    "INTC": "INTC"
}
from_symbol_to_name = {
    "AAPL": "apple",
    "MSFT": "microsoft",
    "AMZN": "amazon",
    "GOOGL": "google",
    "META": "meta",
    "TSLA": "tesla",
    "NVDA": "nvidia",
    "BRK.A": "berkshire hathaway a",
    "BRK.B": "berkshire hathaway b",
    "JPM": "jpmorgan",
    "JNJ": "johnson",
    "V": "visa",
    "PG": "procter & gamble",
    "UNH": "unitedhealth",
    "HD": "home depot",
    "MA": "mastercard",
    "VZ": "verizon",
    "PFE": "pfizer",
    "KO": "coca-cola",
    "DIS": "disney",
    "INTC": "intel"
}
popular_stocks = ['AAPL', 'MSFT', 'TSLA', 'META', 'INTC']
company_names = [
    'Apple',
    'Microsoft Corporation',
    'Tesla',
    'Meta Platforms',
    'Intel Corporation'
]


def update_popular_stocks():
    pass


def get_symbol(stock_name: str) -> str:
    return stocks[stock_name]


def get_actual_price(stock_name: str) -> str:
    stock_symbol = get_symbol(stock_name)
    ticker = yf.Ticker(stock_symbol)
    stock_info = ticker.info
    return stock_info['currentPrice']


# last_popular_stock_price = []


def get_stocks(stock_names: list) -> pd.DataFrame:
    stock_price = {}
    last_know_price = {}
    change = []
    relative_change = []
    old_price = []
    with open("recent_stock_price.json", "r") as file:
        last_know_price = json.load(file)

    for stock in stock_names:
        price = get_actual_price(stock)
        stock_price.update({stock: price})
        if stock in last_know_price:
            old_price.append(last_know_price[stock])
            change.append(last_know_price[stock] - price)
            relative_change.append(change[-1] / last_know_price[stock] * 100)
            last_know_price[stock] = price
        else:
            last_know_price.update({stock: price})
            change.append(None)
    df = pd.DataFrame({'Symbol': stock_names,
                       'Name': [from_symbol_to_name[stock] for stock in stock_names],
                       'Price': stock_price.values(),
                       'Change': change,
                       'Relative Change': relative_change,
                       })

    with open('recent_stock_price.json', 'w') as file:
        json.dump(last_know_price, file)
    file.close()
    return df


# print(get_actual_price('apple'))
# print_stocks(popular_stocks)
# print(get_stocks(["NVDA"]))
