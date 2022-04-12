import logo from './logo.svg';
import React,{Component} from "react";
import './App.css';

class App extends Component {

  render(){
    return(
        <div className="App">
      <header className="App-header">
        <img src={require("../src/76596260_p0.png")} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
    );
  }
}

export default App;
