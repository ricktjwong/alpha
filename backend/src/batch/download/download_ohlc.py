import csv
import os

import numpy as np
import pandas as pd
import yfinance as yf

blacklist = ["AAN"]


def convert_to_ohlc(df, ohlc_writer):
    curr_symbol = ""
    rows = []
    for i in range(len(df)):
        for j in range(0, len(df.columns), 6):
            symbol, column = df.columns[j]
            if df.iloc[i, j] == df.iloc[i, j] and symbol not in blacklist:
                datetime = df.index[i]
                openz = df.iloc[i, j]
                high = df.iloc[i, j + 1]
                low = df.iloc[i, j + 2]
                close = df.iloc[i, j + 3]
                adj_close = df.iloc[i, j + 4]
                volume = int(df.iloc[i, j + 5])

                ohlc_writer.writerow(
                    [datetime, symbol, openz, high, low, close, adj_close, volume]
                )


def download_ohlc():
    try:
        os.remove("./data/ohlc.csv")
    except:
        pass

    df = pd.read_csv("./data/ticker.csv")

    csvfile = open("./data/ohlc.csv", "w", newline="")
    ohlc_writer = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
    ohlc_writer.writerow(
        ["datetime", "symbol", "openz", "high", "low", "close", "adj_close", "volume"]
    )

    for i in range(0, len(df), 100):
        symbol_str = ""
        for symbol in df["Symbol"][i : i + 100]:
            symbol_str += symbol + " "
        symbol_str = symbol_str[:-1]  # Remove tail space
        data = yf.download(symbol_str, period="max", group_by="ticker")
        empty = np.where(
            pd.isnull(data.tail(365))
        )  # Remove Tickers with <1 Year of Data
        data.drop(data.columns[empty[1]], axis=1, inplace=True)
        row_data = convert_to_ohlc(data, ohlc_writer)

    csvfile.close()
