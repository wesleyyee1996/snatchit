import { observer } from 'mobx-react-lite';
import React from 'react';
import GameBoard from './GameBoard';
import NewGame from './NewGame';
import WordForm from './WordForm';

const GameBoardContainer = observer(({gameStore}) => {

  return(
    <>
      <GameBoard gameStore={gameStore}/>
      <WordForm gameStore={gameStore}/> 
      <NewGame gameStore={gameStore}/>
    </>
  )
});

export default GameBoardContainer;