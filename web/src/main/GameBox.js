import React from "react";
import * as GameBackend from "../react-api/GameBackend"
import {withRouter, Link} from "react-router-dom"

class GameBox extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            id: props.match.params.id,
            game: [],
        }


    }

    componentDidMount() {
        this.GetGame();
    }

    GetGame(event) {
        GameBackend.getGame(this.state.id).then((res) => {
            this.setState({game: res[0]},
                () => {
                    if (event === "refresh") {
                        return;
                    }
                });
        });
    }

    renderGame(game){
        console.log(game);
        return (
            <div>
                {game.title}
            </div>
        )
    }

    render() {
        console.log(this.state.game);
        if(this.state.game.length == 0){
            return (
                <div>
                    Loading...
                </div>
            )
        }
        return (
            <div>
                {this.state.game.title}
            </div>
        );
    }
}

export default withRouter(GameBox);