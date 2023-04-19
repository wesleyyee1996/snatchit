import { makeAutoObservable, observable } from "mobx";
import PlayerStore from "./PlayerStore";
import GameAlertsStore from "./GameAlertsStore";
import { io } from "socket.io-client";
import { v4 as uuidv4 } from "uuid";
import NewGameModalStore from "./NewGameModalStore";

class GameStoreImpl {
  fetchedLetterData = false;

  playerStore = new PlayerStore();

  gameAlertsStore = new GameAlertsStore();

  newGameModalStore = new NewGameModalStore(this);

  socket = io("127.0.0.1:8000");

  constructor() {
    makeAutoObservable(this);

    this.createSocketChannels();
    this.getLetterData();
    const tileData = new Map();
    this.tileData = observable.map(tileData);
  }

  createSocketChannels() {
    this.socket.on("connect", () => {
      console.log("connected!");
    });
    this.socket.on("update_game", (data) => {
      this.updateGame(data);
      console.log(data);
    });
    this.socket.on("generate_board", (data) => {
      this.generateBoard(data["game_state"]["tiles_on_board"]);
    });
    this.socket.on("submit_word_valid", (data) => {
      this.gameAlertsStore.setValidWordAlert(data);
      console.log(data);
    });
    this.socket.on("WordIsTooShortException", (data) => {
      this.gameAlertsStore.addWordIsTooShortAlert(data);
    });
    this.socket.on("WordDoesNotExistInDictionaryException", (data) => {
      this.gameAlertsStore.addWordDoesNotExistInDictionaryAlert(data);
    });
    this.socket.on("CannotMakeWordFromGameTilesException", (data) => {
      console.log(data);
    });
  }

  getLetterData() {
    this.socket.emit("generate_board");
  }

  updateGame(game_data) {
    this.updateGameBoard(game_data["game_state"]["tiles_on_board"]);
    this.updatePlayers(game_data["game_state"]["player_store"]["players"]);
  }

  updateGameBoard(tiles_data) {
    Object.entries(tiles_data).forEach(([tile_id, tile_obj]) => {
      if (tile_obj["is_flipped"] === true) {
        this.tileData.get(tile_id).is_flipped = true;
      }
    });
  }

  updatePlayers(player_data) {
    this.playerStore.updatePlayers(player_data, this.tileData);
  }

  generateBoard(data) {
    Object.entries(data).forEach(([tile_id, tile_obj]) => {
      this.tileData.set(tile_id, {
        id: tile_id,
        letter: tile_obj["letter"],
        pos_x: tile_obj["pos_x"],
        pos_y: tile_obj["pos_y"],
        angle: tile_obj["angle"],
        is_flipped: false,
      });
    });
  }

  getNewGame() {
    this.socket.emit("new_game");
  }

  getSubmitWord(wordText, playerId) {
    var data = { word: wordText, player_id: playerId };
    this.socket.emit("word", data);
  }

  postTileFlipped(tileId) {
    var data = { tile_id: tileId };
    this.socket.emit("tile", data);
  }

  getAddNewPlayer(player_name) {
    let player_id = uuidv4();
    this.playerStore.addPlayer(player_id, player_name);
    this.playerStore.setCurrentPlayer(player_id);
    var data = {
      player_name: player_name,
      player_id: player_id,
    };
    this.socket.emit("add_player", data);
  }
}

export const GameStore = new GameStoreImpl();
