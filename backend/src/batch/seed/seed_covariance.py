from datetime import datetime

import numpy as np
import pandas as pd

from models import TickerCovariance
from repositories import TickerCovarianceRepository, TickerOHLCRepository


def seed_covariance(db):

    TickerCovarianceRepository.drop()

    today = datetime.today()
    date_1yr_ago = datetime(today.year - 1, today.month, today.day)

    symbols = TickerOHLCRepository.get_all_symbols()
    symbols = [res[0] for res in symbols]

    df = TickerOHLCRepository.get_by_tickers(symbols, date_1yr_ago)
    cov_mat = np.cov(df.to_numpy().T)

    bp = 100000
    count = 0

    for i in range(len(symbols)):
        for j in range(i, len(symbols)):
            larger = max(symbols[i], symbols[j])
            smaller = min(symbols[i], symbols[j])
            db.session.add(TickerCovariance(larger, smaller, cov_mat[i][j]))

        count += j
        if count > bp:
            db.session.commit()
            bp += 100000
            print(f"Committing. {count} rows has been added as of now.")
    db.session.commit()
    print(f"Finished adding {count} rows.")
