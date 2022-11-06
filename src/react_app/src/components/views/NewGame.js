import React, {useState} from 'react';
import {observer} from 'mobx-react-lite'

const NewGame = observer(({gameStore}) => {

  return (
    <form>
      <button onClick={gameStore.getNewGame()}>New Game</button>
    </form>
  );
});


export default NewGame;