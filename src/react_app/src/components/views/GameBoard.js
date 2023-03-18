import React from 'react';
import styled from 'styled-components'
import { observer } from 'mobx-react-lite';

const StyledGameBoard = styled.div`
  width: 100%;
  // height: 100%;
  // max-width: 60vw;
  // max-height: 60vh;
  // display: flex;
  justify-content: space;
  flex-grow: 1;
  // flex-wrap: wrap;
  // flex-direction: column;
  // margin: 2vh;
  position: relative;
  // top: 50%;
  // left: 60%;
  // transform: translate(-50%, -50%);
  background-color: blue;
`

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