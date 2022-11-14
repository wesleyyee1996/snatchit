import React from 'react';
import { StyledGameBoard } from '../styles/GameBoard.styled';
import { observer } from 'mobx-react-lite';

const GameBoard = observer(({gameStore}) => {
  
  return (
    <>
      <StyledGameBoard>
        {gameStore.shuffledTiles.map((tile) => <div>{tile}</div>)}
      </StyledGameBoard>
    </>
  );
});

export default GameBoard;