import _ from 'lodash';

export const getTickers = (setSearchTickers) => {
  fetch(`${process.env.REACT_APP_DB_URL}/application/ticker`)
    .then((res) => res.json())
    .then((data) => {
      setSearchTickers(data.tickers);
    });
};

export const getApiData = (props) => {
  const {
    tickers,
    setEntireDomain,
    setChartData,
    setRenderLoad,
    setWeights,
  } = props;
  getAllocation(tickers).then(
    (alloc) => {
      setWeights(alloc.allocation);
      handleGetBacktest(alloc, setChartData, setEntireDomain, setRenderLoad);
    },
    (err) => {
      console.log(err);
      setRenderLoad(false);
    },
  );
};

export const getAllocation = (tickers) => {
  const urlString = `${process.env.REACT_APP_DB_URL}/application/allocation`;
  return new Promise((resolve, reject) => {
    fetch(urlString, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json',
      },
      body: JSON.stringify({ stocks: tickers }),
    })
      .then((res) => res.json())
      .then(
        (allocation) => {
          resolve(allocation);
        },
        (err) => {
          reject(err);
        },
      );
  });
};

export const getBacktest = (allocation) => {
  const urlString = `${process.env.REACT_APP_DB_URL}/application/backtest`;
  return new Promise((resolve, reject) => {
    fetch(urlString, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json',
      },
      body: JSON.stringify(allocation),
    })
      .then((res) => res.json())
      .then(
        (json) => {
          resolve(json);
        },
        (err) => {
          reject(err);
        },
      );
  });
};

const handleGetBacktest = (
  alloc,
  setChartData,
  setEntireDomain,
  setRenderLoad,
) => {
  getBacktest(alloc).then(
    (res) => {
      // data: {yyyy/mm/dd: returns}
      const data = res.results.returns;
      const labels = Object.keys(data);
      const returns = Object.values(data);
      const final = [];
      for (var i = 0; i < labels.length; i++) {
        final.push({ x: new Date(labels[i]), y: returns[i] });
      }
      setEntireDomain({
        y: [_.minBy(final, (d) => d.y).y, _.maxBy(final, (d) => d.y).y],
        x: [final[0].x, _.last(final).x],
      });
      setChartData(final);
      setRenderLoad(false);
    },
    (err) => {
      console.log(err);
      setRenderLoad(false);
    },
  );
};
