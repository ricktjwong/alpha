import React, { Component } from 'react';
import AceEditor from 'react-ace';
import './App.css';

import 'brace/mode/python';
import 'brace/theme/monokai';

class App extends Component {
  constructor (props) {
    super(props)

    this.state = {
      code: ''
    }

    this.onChange = this.onChange.bind(this)
    this.compile = this.compile.bind(this)
  }

  onChange (value) {
    console.log('change', value);
    this.setState({ code: value })
  }

  compile () {
    // Make a POST request with this code to api
    console.log(this.state.code)
    fetch('http://localhost:5000/', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        code: this.state.code
      }),
    })
    .then(res => res.json())
    .then(res => {
      console.log(res)
    })
  }

  render() {
    return (
      <div className="App">
        <AceEditor
          mode="python"
          theme="monokai"
          onChange={this.onChange}
          value={this.state.code}
          style={{ height: '90vh', width: '100vw' }}
          editorProps={{$blockScrolling: true}}
        />
        <button onClick={this.compile}>Compile</button>
      </div>
    )
  }
}

export default App;
