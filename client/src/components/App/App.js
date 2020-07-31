import React, { useState } from 'react';
import Search from '../Search';
import Weights from '../Weights';
import Results from '../Results';
import './App.css';

const App = () => {
  const [weights, setWeights] = useState({});
  const [tickers, setTickers] = useState([]);
  return (
    <div className="App">
      <Search
        tickers={tickers}
        setTickers={setTickers}
        weights={weights}
        setWeights={setWeights}
      />
      <Weights weights={weights} setWeights={setWeights} />
      {/* <Results /> */}
    </div>
  );
};

export default App;
