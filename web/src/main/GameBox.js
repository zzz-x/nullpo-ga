import React from "react";
import * as GameBackend from "../react-api/GameBackend"
import {withRouter, Link} from "react-router-dom"

class GameBox extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            id: props.match.params.id,
            game: [],
            comments: [],
            commentUserSet: [],
        }
    }

    componentDidMount() {
        this.GetGame();
        this.GetComments();
    }

    GetGame(event) {
        GameBackend.getGame(this.state.id).then((res) => {
            if(res.status === 'success') {
                this.setState({
                    game: res.data[0]
                })
            }
        });
    }

    GetComments(event) {
        GameBackend.getComments(this.state.id).then((res) => {
            if (res['status'] === 'success') {
                this.setState({
                        comments: res['comments'],
                        commentUserSet: res['users'],
                    },
                    () => {
                        if (event === "refresh") {
                            return;
                        }
                    });
            }
        });
    }

    renderGame(game) {
        return (
            <div>
                {game.game_title}
            </div>
        )
    }

    renderComments(comments, commentUserSet) {
        return (
            <div>
            {/*    render comments with users*/}
                {comments.map((comment, index) => {
                    return (
                        <div key={index}>
                            <div>
                                {commentUserSet[index].user_name}
                            </div>
                            <div>
                                {comment.comment_contents}
                            </div>
                        </div>
                    )
                })}
            </div>
        )
    }

    render() {
        // console.log(this.state.game);
        if (this.state.game.length === 0) {
            return (
                <div>
                    Loading...
                </div>
            )
        }
        return (
            <div>
                {this.renderGame(this.state.game)}
                {this.renderComments(this.state.comments, this.state.commentUserSet)}
            </div>
        );
    }
}

export default withRouter(GameBox);