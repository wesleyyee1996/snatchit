import { makeAutoObservable } from "mobx";
import Player from "../objects/Player";


export default class PlayerStore {

  players = []

  constructor() {
    makeAutoObservable(this)
    const wesPlayer = Player("wesley")
    wesPlayer.addWord("hello")
    wesPlayer.addWord("testing")
    this.players.push(wesPlayer)
  }  

}