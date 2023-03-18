import { makeAutoObservable} from "mobx"
import React from 'react'
import axios from 'axios'
import Tile from "../views/Tile";
import PlayerStore from '../stores/PlayerStore';

class GameStoreImpl {

  tileData = {};

  shuffledTiles = []

  fetchedLetterData = false;

  currentPlayer = 0;

  playerStore = new PlayerStore();

  constructor() {   
    makeAutoObservable(this);
    this.getLetterData();
  }

  getLetterData() {
    async function fetchData() {
      const req = await axios.get('http://127.0.0.1:8000/api/generateBoard');
      return req.data;
    }
    fetchData().then(data => {
    this.tileData = data; 
    this.generateBoard()})    
  }

  generateBoard() {
    var allTiles = [];
    this.tileData.forEach(
      tile => (
        allTiles.push(
          <Tile letter = {tile['letter']} gameStore = {this} inCenter={true} top_pos={tile['pos_y']} left_pos={tile['pos_x']} angle={tile['angle']}/>
        )
      )
    )

    this.shuffledTiles = allTiles.sort(() => Math.random() - 0.5);
  }

  getNewGame() {
    axios.get('http://127.0.0.1:8000/api/newgame').then(
      res => {
        console.log(res);
      }).catch(
      error => {
        console.log(error);
      }
    );
  }

  getSubmitWord(wordText, playerId) {
    async function fetchData() {
      const req = await axios.get('http://127.0.0.1:8000/api/word?word='+wordText+'&player_id='+playerId);
      console.log(req)
      return req.data;
    }
    fetchData().then(data => {
      const isValid = data;
      if (isValid === 'Valid') {
        this.playerStore.addPlayerWord(wordText, playerId);
      }
    })
  }

  postTileFlipped(letter) {
    axios.post('http://127.0.0.1:8000/api/tile/'+letter).then(
      res => {
        console.log(res);
      }).catch(
      error => {
        console.log(error)
    });
  }


}

export const GameStore = new GameStoreImpl();

