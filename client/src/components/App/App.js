import React, { useState } from 'react';
import Search from '../Search';
import Weights from '../Weights';
import Chart from '../Chart';
import Spinner from 'react-bootstrap/Spinner';
import Button from 'react-bootstrap/Button';
import { getApiData } from '../apiHandler';
import './App.css';
import _ from 'lodash';

const App = () => {
  const [weights, setWeights] = useState({});
  const [tickers, setTickers] = useState([]);
  const [renderLoad, setRenderLoad] = useState(false);
  const [chartData, setChartData] = useState([]);
  const [entireDomain, setEntireDomain] = useState({});
  const getChartData = () => {
    getApiData({ tickers, setEntireDomain, setChartData, setRenderLoad });
    setRenderLoad(true);
  };
  return (
    <div className="App">
      <Search
        tickers={tickers}
        setTickers={setTickers}
        weights={weights}
        setWeights={setWeights}
      />
      <Button variant="primary" onClick={getChartData}>
        Render Chart
      </Button>
      {renderLoad && (
        <div style={style.space}>
          <Spinner animation="border" variant="primary">
            <span className="sr-only">Loading...</span>
          </Spinner>
        </div>
      )}
      {!renderLoad && chartData.length != 0 && (
        <Chart data={chartData} entireDomain={entireDomain} maxPoints={300} />
      )}
    </div>
  );
};

const style = {
  space: {
    marginTop: 20,
  },
};

export default App;
