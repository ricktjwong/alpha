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
    all_history = {}
    for symbol in symbols:
        all_history[symbol] = []
    for row in TickerOHLCRepository.get_by_tickers(symbols, date_1yr_ago):
        all_history[row[0]].append(row[1])

    df = pd.DataFrame(all_history)
    cov_mat = np.cov(df.to_numpy().T)

    for i in range(len(symbols)):
        for j in range(i, len(symbols)):
            db.session.add(TickerCovariance(symbols[i], symbols[j], cov_mat[i][j]))
        db.session.commit()
        count += j
