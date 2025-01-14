import scrape_investor_data as sc
import input_with_help as iwh
import json
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

popular_stocks = ['AAPL', 'MSFT', 'TSLA', 'META', 'INTC']


# def invest_into_stock(username: str):
#     # stock = sc.get_symbol(iwh.input_with_help("Choose stock to invest"))
#     stock = input("apple\n")
#     amount = input("Enter amount\n")
#     account = {username: "password"}
#     with open("account.json", "r") as file:
#         account = json.load(file)
#     if stock in account:
#         account[stock] += float(amount) / float(sc.get_actual_price(stock))
#     else:
#         account.update({stock: float(amount) / float(sc.get_actual_price(stock))})
#     with open("account.json", "w") as file:
#         json.dump(account, file)


def invest_into_stock_visual(username: str,stock,amount):
    # stock = sc.get_symbol(iwh.input_with_help("Choose stock to invest"))
    account = {username: "password"}
    with open("account.json", "r") as file:
        account = json.load(file)
    if stock in account:
        account[stock] += float(amount) / float(sc.get_actual_price(stock))
    else:
        account.update({stock: float(amount) / float(sc.get_actual_price(stock))})
    with open("account.json", "w") as file:
        json.dump(account, file)



def investments_overview() -> tuple:
    account = {}
    with open("account.json", "r") as file:
        account = json.load(file)
    last_value = account["current_value"]

    df_stocks_overview = sc.get_stocks(list(account.keys())[2:])
    df_stocks_overview['Owned shares'] = list(account.values())[2:]

    portfolio_value = df_stocks_overview.apply(lambda row: float(row['Price']) * float(row['Owned shares']),
                                               axis=1).sum()
    # print(df_stocks_overview)

    df_stocks_overview['Owned shares'] = [round(amount, 4) for amount in df_stocks_overview['Owned shares']]

    total_change = float(portfolio_value) - float(last_value)
    relative_change = total_change * 100 / last_value
    df_total_overview = pd.DataFrame(
        {'Portfolio value': [portfolio_value], 'Change': [total_change], 'Relative change': [relative_change]})
    # print(df_total_overview)
    account["current_value"] = portfolio_value
    with open("account.json", "w") as file:
        json.dump(account, file)
    file.close()
    ret = tuple([df_stocks_overview,df_total_overview])
    return ret

def investing_menu():
    print('-------------Welcome to your investments---------------')
    print('1. Current market (popular stock)')
    print('2. Your investments')
    print('3. Invest in stock')
    print('4. To Exit')
    print('-------------------------------------------------------')
    choice = input('Choose number')
    invest_menu = True
    while invest_menu:
        if choice == '1':
            sc.update_popular_stocks()
            print(sc.get_stocks(popular_stocks))
            if input("press c to continue") == 'c':
                pass
        if choice == '2':
            pass
        if choice == '3':
            invest_into_stock("Guest")
        if choice == '4':
            break


# investing_menu()
# invest_into_stock("Guest")
# print(investments_overview()[0])
