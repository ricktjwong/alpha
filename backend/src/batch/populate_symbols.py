import pandas as pd

from repositories import TickerRepository


def populate_symbols():

    # Delete existing information
    TickerRepository.drop()

    # Populate from data file
    df = pd.read_csv("./data/symbols.csv")
    for symbol in df["Symbol"].to_numpy():
        TickerRepository.create(symbol)
