import React from 'react';
import GameBoard from './GameBoard';
import NewGame from './NewGame';
import WordForm from './WordForm';

const GameBoardContainer = () => {
  return(
    <>
      <GameBoard/>
      <WordForm/> 
      <NewGame/>
    </>
  )
};

export default GameBoardContainer;