import { makeAutoObservable } from "mobx";
import Player from "../objects/Player";

export default class PlayerStore {
  players = new Map();

  currentPlayer = undefined;

  constructor() {
    makeAutoObservable(this);
  }

  addPlayerWord(word, playerId) {
    this.getPlayerById(playerId).addWord(word);
  }

  removePlayerWord(word, playerId) {
    this.getPlayerById(playerId).removeWord(word);
  }

  addPlayer(playerId, playerName) {
    if (!this.players.has(playerId)) {
      this.players.set(playerId, new Player(playerId, playerName));
    }
  }

  updatePlayers(player_data, tile_data) {
    Object.entries(player_data).forEach(([player_id, player_obj]) => {
      this.addPlayer(player_id, player_obj["name"]);
      const words = player_obj["words"];
      if (Object.keys(words).length > 0) {
        Object.values(words).forEach((word_obj) => {
          Object.values(word_obj).forEach((tile) => {
            if (tile_data.has(tile["id"])) {
              tile_data.delete(tile["id"]);
            }
          });
        });
      }
      this.getPlayerById(player_id).updateWords(words);
    });
  }

  setCurrentPlayer(player_id) {
    if (this.currentPlayer === undefined) {
      this.currentPlayer = this.players.get(player_id);
    }
  }

  getCurrentPlayer() {
    if (this.currentPlayer !== undefined) {
      return this.currentPlayer.id;
    }
  }

  getPlayersList() {
    return Array.from(this.players.values());
  }

  getPlayerById(playerId) {
    if (!this.players.has(playerId)) {
      throw new Error(
        "Player store doesn't have player with id" + playerId + "!"
      );
    }
    return this.players.get(playerId);
  }

  numPlayers() {
    return this.players.size;
  }
}
