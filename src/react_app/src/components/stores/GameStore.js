import { makeAutoObservable, observable } from "mobx";
import React from "react";
import axios from "axios";
import Tile from "../objects/Tile";
import PlayerStore from "../stores/PlayerStore";

class GameStoreImpl {
  fetchedLetterData = false;

  currentPlayer = 0;

  playerStore = new PlayerStore();

  constructor() {
    makeAutoObservable(this);
    this.getLetterData();
    setTimeout(() => {this.getAddNewPlayer(0, 'Wes');}, 1000)
    setTimeout(() => {this.getAddNewPlayer(1, 'Janice');}, 1000)
    const tileData = new Map();
    this.tileData = observable.map(tileData);
  }

  getLetterData() {
    async function fetchData() {
      const req = await axios.get("http://127.0.0.1:8000/api/generateBoard");
      return req.data;
    }
    fetchData().then((data) => {
      this.generateBoard(data["game_state"]["tiles_on_board"]);
    });
  }

  updateGame(game_data) {
    this.updateGameBoard(game_data["game_state"]["tiles_on_board"])
    this.updatePlayers(game_data["game_state"]["player_store"]["players"])
  }

  updateGameBoard(tiles_data) {
    Object.entries(tiles_data).forEach(([tile_id, tile_obj]) => {
      if (tile_obj["is_flipped"]) {
        this.tileData.get(tile_id).setIsFlipped(true)
      }
    });
  }

  updatePlayers(player_data) {
    Object.entries(player_data).forEach(([player_id, player_obj]) => {
      this.playerStore.addPlayer(player_id, player_obj["name"])
      const words = player_obj["words"]
      if (Object.keys(words).length > 0) {
        Object.entries(words).forEach(([word, word_obj]) => {
          Object.values(word_obj).forEach((tile) => {
            this.tileData.delete(tile["id"])
          });
          this.playerStore.addPlayerWord(word, player_id)
        });
      }
      if (this.playerStore.currentPlayer == null) {
        this.playerStore.currentPlayer = this.playerStore.players.get(player_id)
      }
    });
  }

  generateBoard(data) {
    Object.entries(data).forEach(([tile_id, tile_obj]) => {
      this.tileData.set(
        tile_id,
        new Tile(
          tile_id,
          tile_obj["letter"],
          true,
          tile_obj["pos_x"],
          tile_obj["pos_y"],
          tile_obj["angle"]
        )
      );
    });
  }

  getNewGame() {
    axios
      .get("http://127.0.0.1:8000/api/newGame")
      .then((res) => {
        this.updateGame(res.data)
      })
      .catch((error) => {
        console.log(error);
      });
  }

  getSubmitWord(wordText, playerId) {
    async function fetchData() {
      const res = await axios.get(
        "http://127.0.0.1:8000/api/word?word=" +
          wordText +
          "&player_id=" +
          playerId
      );
      // console.log(req);
      return res.data;
    }
    fetchData().then((data) => {
      this.updateGame(data)
    });
  }

  postTileFlipped(tile_id) {
    axios
      .get("http://127.0.0.1:8000/api/tile?tile_id=" + tile_id)
      .then((res) => {
        this.updateGame(res.data)
      })
      .catch((error) => {
        console.log(error);
      });
  }

  getAddNewPlayer(player_id, player_name) {
    async function fetchData() {
      const res = await axios.get(
        "http://127.0.0.1:8000/api/addPlayer?player_name=" +
        player_name + "&player_id=" + player_id
      );
      return res.data;
    }
    fetchData().then((data) => {
      this.updateGame(data)
    });
  }
}

export const GameStore = new GameStoreImpl();
