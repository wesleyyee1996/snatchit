import { makeAutoObservable } from "mobx";
import Player from "../objects/Player";


export default class PlayerStore {

  players = []

  constructor() {
    makeAutoObservable(this)
    const wesPlayer = new Player("wesley")
    wesPlayer.addWord("hello")
    wesPlayer.addWord("testing")
    this.players.push(wesPlayer)
    const janicePlayer = new Player("janice");
    janicePlayer.addWord("hahaha")
    janicePlayer.addWord("aku")
    janicePlayer.addWord("cinta")
    janicePlayer.addWord("kamu")
    this.players.push(janicePlayer)
  }  

}