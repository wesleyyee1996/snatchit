import { makeAutoObservable } from "mobx";
import React from "react";
import axios from "axios";
import Tile from "../objects/Tile";
import PlayerStore from "../stores/PlayerStore";

class GameStoreImpl {
  tileData = new Map();

  fetchedLetterData = false;

  currentPlayer = 0;

  playerStore = new PlayerStore();

  constructor() {
    makeAutoObservable(this);
    this.getLetterData();
  }

  getLetterData() {
    async function fetchData() {
      const req = await axios.get("http://127.0.0.1:8000/api/generateBoard");
      return req.data;
    }
    fetchData().then((data) => {
      this.generateBoard(data);
    });
  }

  generateBoard(data) {
    data.forEach((tile) => {
      this.tileData.set(
        tile["id"],
        new Tile(
          tile["id"],
          tile["letter"],
          true,
          tile["pos_x"],
          tile["pos_y"],
          tile["angle"]
        )
      );
    });
  }

  getNewGame() {
    axios
      .get("http://127.0.0.1:8000/api/newgame")
      .then((res) => {
        console.log(res);
      })
      .catch((error) => {
        console.log(error);
      });
  }

  getSubmitWord(wordText, playerId) {
    async function fetchData() {
      const req = await axios.get(
        "http://127.0.0.1:8000/api/word?word=" +
          wordText +
          "&player_id=" +
          playerId
      );
      // console.log(req);
      return req.data;
    }
    fetchData().then((data) => {
      console.log(data);
      const isValid = data["is_valid"];
      const tilesMoved = data["tiles_moved"];
      if (isValid === true) {
        tilesMoved.forEach((tile_id) => {
          // console.log("tiles moved", tile_id, this.tileData.get(tile_id));
          console.log("test", this.tileData);
          this.tileData.data_.get(tile_id).isHidden = true;
        });
        this.playerStore.addPlayerWord(wordText, playerId);
      }
    });
  }

  postTileFlipped(tile_id) {
    axios
      .post("http://127.0.0.1:8000/api/tile?tile_id=" + tile_id)
      .then((res) => {
        console.log(res);
      })
      .catch((error) => {
        console.log(error);
      });
  }
}

export const GameStore = new GameStoreImpl();
