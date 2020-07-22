import pandas as pd

from repositories import TickerRepository


def populate_tickers():

    # Delete existing information
    TickerRepository.drop()

    # Populate from data file
    df = pd.read_csv("./data/ticker.csv")
    for row in df.iterrows():
        symbol = row[1]['Symbol']
        mcap = row[1]['mcap']
        TickerRepository.create(symbol, mcap)
