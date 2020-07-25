import React from 'react';
import { Multiselect } from 'multiselect-react-dropdown';

class SearchComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      options: [],
    };
    this.style = {
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
  }

  componentDidMount() {
    fetch('http://localhost:3000/application/ticker')
      .then((res) => res.json())
      .then((data) => {
        this.setState({ options: data.tickers });
      });
  }

  onSearch(search) {
    this.state.tickers.filter((x) => {
      x.contains(search);
    });
  }

  onSelect(selectedList, selectedItem) {
    // On confirmation conduct backtest on selected list on stocks with weights
    console.log(selectedList);
    console.log(selectedItem);
  }

  onRemove(selectedList, removedItem) {
    console.log(selectedList);
    console.log(removedItem);
  }

  render() {
    if (this.state.options.length == 0) return null;
    else {
      return (
        <Multiselect
          placeholder="Choose ticker"
          options={this.state.options}
          selectedValues={this.state.selectedValue}
          onSelect={this.onSelect}
          onRemove={this.onRemove}
          isObject={false}
          style={this.style}
        />
      );
    }
  }
}

export default SearchComponent;
