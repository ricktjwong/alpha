import _ from 'lodash';

export const getApiData = (props) => {
  const { tickers, setEntireDomain, setChartData, setRenderLoad } = props;
  // Pass tickers to backend and get weights and backtest
  // as response
  const apiKey = process.env.REACT_APP_ALPHAVANTAGE_APIKEY;
  const ticker = 'AAPL';
  const urlString =
    'https://www.alphavantage.co/query?function=' +
    'TIME_SERIES_DAILY_ADJUSTED&' +
    'symbol=' +
    ticker +
    '&outputsize=full&apikey=' +
    apiKey;
  fetch(urlString)
    .then((res) => res.json())
    .then((json) => {
      let stockData = json['Time Series (Daily)'];
      const labels = Object.keys(stockData).reverse();
      const values = Object.values(stockData).reverse();
      const data = values.map((x) => parseFloat(x['5. adjusted close']));
      const final = [];
      for (var i = 0; i < data.length; i++) {
        final.push({ x: new Date(labels[i]), y: data[i] });
      }
      setEntireDomain({
        y: [_.minBy(final, (d) => d.y).y, _.maxBy(final, (d) => d.y).y],
        x: [final[0].x, _.last(final).x],
      });
      setChartData(final);
      setRenderLoad(false);
    });
};
