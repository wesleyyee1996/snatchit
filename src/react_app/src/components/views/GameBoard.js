import React from "react";
import styled from "styled-components";
import { observer } from "mobx-react-lite";

const StyledGameBoard = styled.div`
  width: 100%;
  justify-content: space;
  flex-grow: 1;
  position: relative;
  background-color: blue;
`;

const GameBoard = observer(({ gameStore }) => {
  return (
    <>
      <StyledGameBoard>
        {Array.from(gameStore.tileData.values()).map((tile) => (
          <div>{tile}</div>
        ))}
      </StyledGameBoard>
    </>
  );
});

export default GameBoard;
