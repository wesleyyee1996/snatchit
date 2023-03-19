import React from "react";
import styled from "styled-components";
import { observer } from "mobx-react-lite";
import Tile from "../views/Tile";

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
          <div>
            <Tile gameStore={gameStore} tileObj={tile}></Tile>
          </div>
        ))}
      </StyledGameBoard>
    </>
  );
});

export default GameBoard;
