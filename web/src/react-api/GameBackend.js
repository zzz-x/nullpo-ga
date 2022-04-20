import * as Setting from "../Setting"
export function getGames(){
    // alert(`${Setting.ServerUrl}/api/get-all-games`);
    return fetch(`${Setting.ServerUrl}/api/get-all-games`,{
        method: "GET",
        credentials: "include",
        }).then((res)=>res.json());
}

export function getGame(id){
    // alert(`${Setting.ServerUrl}/api/get-game?game_id=${id}`);
    return fetch(`${Setting.ServerUrl}/api/get-game?game_id=${id}`,{
        method: "GET",
        credentials: "include",
        }).then((res)=>res.json());
}

export function getComments(id){
    // alert(`${Setting.ServerUrl}/api/get-comments?game_id=${id}`);
    return fetch(`${Setting.ServerUrl}/api/game/get-comments?game_id=${id}`,{
        method: "GET",
        credentials: "include",
        }).then((res)=>res.json());
}
