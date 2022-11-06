import { makeAutoObservable} from "mobx"
import React from 'react'
import axios from 'axios'

class GameStoreImpl {

  letterJsonData = {};

  constructor() {   
    makeAutoObservable(this);
  }

  getLetterData() {
    async function fetchData() {
      const req = await axios.get('http://127.0.0.1:8000/api/generateBoard');
      return req.data;
    }
    fetchData().then(data => this.letterJsonData = data);
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

  getSubmitWord(wordText) {
    axios.get('http://127.0.0.1:8000/api/word/'+wordText).then(
      res => {
        console.log(res);
      }).catch(
      error => {
        console.log(error);
      }
    );
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

