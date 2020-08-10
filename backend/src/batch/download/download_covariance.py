import os
import csv
from datetime import datetime

import numpy as np
import pandas as pd

from models import TickerCovariance
from repositories import TickerOHLCRepository


def download_covariance():
    try:
        os.remove("./data/covariance.csv")
    except:
        pass

    today = datetime.today()
    date_1yr_ago = datetime(today.year - 1, today.month, today.day)

    symbols = TickerOHLCRepository.get_all_symbols()
    symbols = [res[0] for res in symbols]

    df, _ = TickerOHLCRepository.get_by_tickers(symbols, date_1yr_ago)
    cov_mat = np.cov(df.to_numpy().T)

    csvfile = open("./data/covariance.csv", "w", newline="")
    ohlc_writer = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
    ohlc_writer.writerow(
        ["symbol1", "symbol2", "covariance"]
    )

    for i in range(len(symbols)):
        for j in range(i, len(symbols)):
            larger = max(symbols[i], symbols[j])
            smaller = min(symbols[i], symbols[j])
            ohlc_writer.writerow(
                [larger, smaller, cov_mat[i][j]]
            )

    csvfile.close()
