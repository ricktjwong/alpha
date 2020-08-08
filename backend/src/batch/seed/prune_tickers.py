from models import Ticker
from repositories import TickerOHLCRepository, TickerRepository


def prune_tickers(db):
    symbols = [ticker.json["symbol"] for ticker in TickerRepository.get_all()]
    symbols_ohlc = [symbol[0] for symbol in TickerOHLCRepository.get_all_symbols()]
    diff_symbols = list(set(symbols) - set(symbols_ohlc))
    db.session.query(Ticker).filter(Ticker.symbol.in_(diff_symbols)).delete(
        synchronize_session=False
    )
    db.session.commit()
