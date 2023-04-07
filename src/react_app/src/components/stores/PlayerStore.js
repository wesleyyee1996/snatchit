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

  removePlayerWord(word, playerId) {
    this.players.get(playerId).removeWord(word);
  }

  addPlayer(playerId, playerName) {
    if (!this.players.has(playerId)) {
      this.players.set(playerId, new Player(playerId, playerName))
    }
  }

  updatePlayers(player_data, tile_data) {
    Object.entries(player_data).forEach(([player_id, player_obj]) => {
      this.addPlayer(player_id, player_obj["name"])
      const words = player_obj["words"]
      if (Object.keys(words).length > 0) {
        Object.values(words).forEach((word_obj) => {
          Object.values(word_obj).forEach((tile) => {
            if (tile_data.has(tile["id"])) {
              tile_data.delete(tile["id"])
            }
          });
        });
      }
      this.players.get(player_id).updateWords(words)
      if (this.currentPlayer == null) {
        this.currentPlayer = this.players.get(player_id)
      }
    });
  }
}
