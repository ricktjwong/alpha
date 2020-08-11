import React, { useState } from 'react';
import Search from '../Search';
import Caption from '../Caption';
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
  const [theme, setTheme] = useState('light');
  const getChartData = () => {
    getApiData({
      tickers,
      setEntireDomain,
      setChartData,
      setRenderLoad,
      setWeights,
    });
    setRenderLoad(true);
  };
  return (
    <div
      className="App"
      style={style[theme].app}>
      <Search
        tickers={tickers}
        setTickers={setTickers}
        weights={weights}
        setWeights={setWeights}
        style={style[theme].searchComponent}
      />
      <Button variant="primary" onClick={getChartData} style={style[theme].button}>
        Render Chart
      </Button>
      {renderLoad && (
        <div style={style[theme].space}>
          <Spinner animation="border" variant="primary">
            <span className="sr-only">Loading...</span>
          </Spinner>
        </div>
      )}
      {!renderLoad && chartData.length != 0 && (
        <div style={style[theme].card}>
          <Chart data={chartData} entireDomain={entireDomain} maxPoints={300} />
          <Caption weights={weights} />
        </div>
      )}
    </div>
  );
};

const style = {
  light: {
    app: {
      backgroundColor: 'white',
      height: '100vh',
      width: '100vw',
      padding: 30,
    },
    button: {
      marginBottom: 20,
    },
    searchComponent: {
      margin: 20,
    },
    space: {
      marginTop: 20,
    },
    card: {
      display: 'flex',
      flexDirection: 'row',
      flexWrap: 'wrap',
      alignItems: 'center',
      justifyContent: 'center',
      backgroundColor: 'rgba(242, 241, 239, 0.6)',
      width: '60vw',
      margin: '0 auto',
      borderRadius: 10,
    },
  },
  dark: {
    card: {
      backgroundColor: 'rgba(255, 255, 255, 0.6)',
    }
  }
};

export default App;
