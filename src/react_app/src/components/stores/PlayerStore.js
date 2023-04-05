import { makeAutoObservable } from "mobx";
import Player from "../objects/Player";

export default class PlayerStore {
  players = new Map();

  currentPlayer = null;

  constructor() {
    makeAutoObservable(this);
    // const wesPlayer = new Player("wesley");
    // wesPlayer.addWord("hello");
    // wesPlayer.addWord("testing");
    // this.players.set(1, wesPlayer);
    // const janicePlayer = new Player("janice");
    // janicePlayer.addWord("hahaha");
    // janicePlayer.addWord("aku");
    // janicePlayer.addWord("cinta");
    // janicePlayer.addWord("kamu");
    // this.players.set(2, janicePlayer);
    // this.currentPlayer = this.players.get(1);
  }

  addPlayerWord(word, playerId) {
    this.players.get(playerId).addWord(word);
  }

  addPlayer(playerId, playerName) {
    if (!this.players.has(playerId)) {
      this.players.set(playerId, new Player(playerId, playerName))
    }
  }
}
