import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';
import { defaults } from 'react-chartjs-2';

defaults.global.defaultFontSize = 10;

export default (Results) => {
  const [chartData, setChartData] = useState(null);
  useEffect(() => {
    getData().then((json) => {
      json = json['Time Series (Daily)'];
      const labels = Object.keys(json);
      const values = Object.values(json);
      const data = values.map((x) => parseFloat(x['5. adjusted close']));
      console.log(labels);
      const chart = {
        labels: labels.reverse(),
        datasets: [populateChart('AAPL', data)],
      };
      setChartData(chart);
    });
  }, []);
  if (!chartData) {
    return null;
  } else {
    return (
      <div>
        <div
          style={{
            width: '90vw',
            height: '60vh',
            margin: '0 auto',
          }}>
          <Line
            data={chartData}
            options={{
              scales: {
                xAxes: [
                  {
                    ticks: {
                      autoSkip: true,
                      maxTicksLimit: 20,
                    },
                  },
                ],
              },
            }}
          />
        </div>
      </div>
    );
  }
};

const populateChart = (ticker, data) => {
  return {
    label: ticker,
    fill: false,
    redraw: true,
    lineTension: 0.1,
    backgroundColor: 'rgba(75,192,192,0.4)',
    borderColor: 'rgba(75,192,192,1)',
    borderCapStyle: 'butt',
    borderDash: [],
    borderDashOffset: 0.0,
    borderJoinStyle: 'miter',
    pointBorderColor: 'rgba(75,192,192,1)',
    pointBackgroundColor: '#fff',
    pointBorderWidth: 1,
    pointHoverRadius: 5,
    pointHoverBackgroundColor: 'rgba(75,192,192,1)',
    pointHoverBorderColor: 'rgba(220,220,220,1)',
    pointHoverBorderWidth: 2,
    pointRadius: 1,
    pointHitRadius: 10,
    data: data.reverse(),
  };
};

const getData = () => {
  var promise = new Promise((resolve, reject) => {
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
      .then((data) => {
        resolve(data);
      })
      .catch((error) => {
        reject(error);
      });
  });
  return promise;
};
