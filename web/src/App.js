import logo from './logo.svg';
import React, {Component} from "react";
import {Switch, Route} from "react-router-dom"
import './App.css';
import GameListBox from "./main/GameListBox";
import GameBox from "./main/GameBox";

class App extends Component {
    renderMain() {
        return (
            <Switch>
                <Route exact path="/">
                    <GameListBox/>
                </Route>
                <Route path="/game/:id">
                    <GameBox/>
                </Route>
            </Switch>
        )
    }

    render() {
        return (
            <div className="App">
                {this.renderMain()}
            </div>
        );
    }
}

export default App;
