import React, { useEffect, useState } from 'react';
import { Multiselect } from 'multiselect-react-dropdown';

const Search = (props) => {
  const [searchTickers, setSearchTickers] = useState([]);

  useEffect(() => {
    fetch('http://localhost:3000/application/ticker')
      .then((res) => res.json())
      .then((data) => {
        setSearchTickers(data.tickers);
      });
  }, []);

  const updateTickerAndWeights = (tickers) => {
    var weights = {};
    tickers.forEach((x) => {
      weights[x] = 1.0 / tickers.length;
    });
    props.setTickers(tickers);
    props.setWeights(weights);
  };

  const onSelect = (selectedList, selectedItem) => {
    // On confirmation conduct backtest on selected list on stocks with weights
    updateTickerAndWeights(selectedList);
  };

  const onRemove = (selectedList, removedItem) => {
    updateTickerAndWeights(selectedList);
  };

  if (searchTickers.length == 0) return null;
  else {
    return (
      <>
        <Multiselect
          placeholder="Choose tickers"
          options={searchTickers}
          onSelect={onSelect}
          onRemove={onRemove}
          isObject={false}
          style={style}
        />
      </>
    );
  }
};

const style = {
  searchBox: {
    width: '50vw',
    margin: '0 auto',
    marginTop: 20,
    marginBottom: 20,
  },
  optionContainer: {
    width: '50vw',
    margin: '0 auto',
  },
  inputField: {
    fontSize: 20,
  },
};

export default Search;
