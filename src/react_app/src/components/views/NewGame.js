import React from 'react';
import {observer} from 'mobx-react-lite'

const NewGame = observer(({gameStore}) => {

  return (
    <form>
      <button class="btn btn-primary" onClick={gameStore.getNewGame()}>New Game</button>
    </form>
  );
});


export default NewGame;