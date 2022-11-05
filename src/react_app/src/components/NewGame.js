import React, {useState} from 'react';
import axios from 'axios';

const NewGame = () => {

  function newGame(e) {
    axios.get('http://127.0.0.1:8000/api/newgame').then(
      res => {
        console.log(res);
      }).catch(
      error => {
        console.log(error);
      }
    );
  }

  return (
    <form>
      <button onClick={e => newGame(e)}>New Game</button>
    </form>
  );
};


export default NewGame;