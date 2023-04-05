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
  const renderTiles = (tilesMap) => {
    const tilesComps = [];
    tilesMap.forEach((tileObj, tile_id) =>
      tilesComps.push(
        <div>
          <Tile key={tile_id} gameStore={gameStore} tileObj={tileObj}></Tile>
        </div>
      )
    );
    return tilesComps;
  };

  return (
    <>
      <StyledGameBoard>{renderTiles(gameStore.tileData)}</StyledGameBoard>
    </>
  );
});

export default GameBoard;
