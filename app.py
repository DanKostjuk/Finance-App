import tkinter as tk
# from tkinter import ttk
# import customtkinter as ctk
# from matplotlib.widgets import Button
from pandastable import Table, TableModel
import scrape_investor_data as sc
import investing
# import pandas as pd
# from pyrr.rectangle import width

# import finance_app as fa
root = tk.Tk()
root.geometry('1000x600')
popular_stocks = ['AAPL', 'MSFT', 'TSLA', 'META', 'INTC']


def exit(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    frame.destroy()
def exitForButton(frame,button):
    exit(frame)
    button.place_forget()

def portfolio():
    frame = tk.Frame(root, padx=20, background='#ffffff')
    frame.place(relx=.5, rely=.3, anchor="c")
    # frame.rowconfigure(0, weight=1)
    # frame.columnconfigure(0, weight=1)
    tmp = investing.investments_overview()
    df = tmp[0]
    df2 = tmp[1]
    columsDf2 = list(df2.columns)
    columsDf2.extend(['','',''])
    firstRow = list(df2.iloc[0])
    firstRow.extend(['','',''])
    df.loc[len(df)] = columsDf2
    df.loc[len(df)] = firstRow

    frame.pt = Table(frame,width=800, dataframe=df)
    frame.pt.show()
    exitButton = tk.Button(root, bg='#48f542', text='Back', command=lambda: exitForButton(frame, exitButton))
    exitButton.place(relx=.5, rely=.5, anchor="c")

def currentMarket():
    frame = tk.Frame(root, padx=20, background='#ffffff')
    frame.place(relx=.5, rely=.2, anchor="c")
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    exitButton = tk.Button(root,bg='#48f542', text='Back', command=lambda :exitForButton(frame,exitButton))
    df = sc.get_stocks(popular_stocks)
    frame.pt = Table(frame,dataframe=df)
    frame.pt.show()
    exitButton.place(relx=.5, rely=.5, anchor="c")


def invest():
    def investInput():
        stock = sc.get_symbol(textBoxName.get('1.0',tk.END).strip())
        amout = textBoxAmout.get('1.0', tk.END).strip()
        investing.invest_into_stock_visual("name",stock,amout)

    frame = tk.Frame(root, padx=20,pady=25, background='#ffffff')
    frame.place(relx=.5, rely=.2, anchor="c")
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    nameLabel = tk.Label(frame,background='#ffffff',text='Stock Name:')
    nameLabel.grid(row=0,column=0)
    textBoxName = tk.Text(frame, height = 1, width = 15)
    textBoxName.grid(row=0,column=1)
    AmoutLabel = tk.Label(frame,background='#ffffff',text='Invested Amount:')
    AmoutLabel.grid(row=1,column=0)
    textBoxAmout = tk.Text(frame, height = 1, width = 15)
    textBoxAmout.grid(row=1,column=1)
    investButton = tk.Button(frame,pady=5,text='invest',command=investInput)
    investButton.grid(row=2,column=1)
    exitButton = tk.Button(root,bg='#48f542', text='Back', command=lambda :exitForButton(frame,exitButton))
    exitButton.place(relx=.5, rely=.5, anchor="c")

def investingMenu():
    frame = tk.Frame(root,padx=20, background='#ffffff')
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)
    frame.rowconfigure(3, weight=1)

    frame.lable1 = tk.Button(frame,bg='#48f542', text='Portfolio',command=portfolio)
    frame.lable2 = tk.Button(frame,bg='#48f542', text='Current Market',command=currentMarket)
    frame.lable3 = tk.Button(frame,bg='#48f542', text='Invest',command=invest)
    lable4 = tk.Button(root,bg='#48f542', text='Back', command=lambda :exit(frame))
    frame.place(relx=.5, rely=.2, anchor="c")

    frame.lable1.grid(row=0)
    frame.lable2.grid(row=1)
    frame.lable3.grid(row=2)
    lable4.place(relx=.5, rely=.5, anchor="c")



investinButton = tk.Button(root, text='investing menu', command=investingMenu)

# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=1)
# root.columnconfigure(2, weight=1)

investinButton.place(relx=.5, rely=.2,anchor="c")

root.mainloop()
