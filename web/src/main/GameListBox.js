import * as GameBackend from "../react-api/GameBackend"
import {Link} from "react-router-dom"
import React from "react";

class GameListBox extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            games: [],
        }
    }

    getGames(event) {
        GameBackend.getGames().then((res) => {
            this.setState(
                {
                    games: res,
                },
                () => {
                    if (event === "refresh") {
                        return;
                    }
                }
            )
        });

    }

    componentDidMount() {
        this.getGames();
    }

    renderGame(game, index) {
        return (
            <div id="aGame" className="animate__animated animate__bounceInUp">
                <Link to={"/game?gameid=" + game.id}>
                    <img id="gameCover" src={require("../static/gameMaterialStock/"+game.id+"/game_cover.png")}/>
                </Link>
                <div id="gameTextBox">
                    <p id="gamerank">Rank {index}</p>
                    <Link to={"/game/" + game.id}>
                        <p className="animate__animated animate__bounce" id="gameTitle"
                           className="animate__headShake"> {game.title}</p>
                    </Link>

                </div>
                <p id="gameUpdateTime">release
                    time:{game.release_time.year}年{game.release_time.month}月{game.release_time.day}日</p>
                <div className="collectButton">
                    <button id={game['id']} onClick="collect('{{game.game_id}}')" className="btn btn-primary"
                            type="button" value="{{game.game_id}}">
                        😘
                    </button>
                </div>
            </div>
        );
    }

    render() {
        return (
            <div>
                {this.state.games?.map((game) => {
                    return this.renderGame(game, this.state.games.indexOf(game) + 1);
                })}
            </div>
        )
    }
}

export default GameListBox;