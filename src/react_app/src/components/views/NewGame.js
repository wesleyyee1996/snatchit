import React, {useState} from 'react';
import {observer} from 'mobx-react-lite'
import axios from 'axios';

const NewGame = observer(({gameStore}) => {

  return (
    <form>
      <button onClick={gameStore.getNewGame()}>New Game</button>
    </form>
  );
});


export default NewGame;