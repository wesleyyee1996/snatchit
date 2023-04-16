import React, { useState } from "react";
import {
  StyledTile,
  StyledCenterTile,
  StyledPlayerTile,
} from "../styles/Tile.styled";
import { StyledTileLetter } from "../styles/TileLetter.styled";
import { observer } from "mobx-react-lite";

const Tile = observer(({ gameStore, tileObj }) => {
  const sendFlipped = () => {
    if (tileObj.is_flipped === true) {
      return;
    }
    gameStore.postTileFlipped(tileObj.id);
    tileObj.is_flipped = true;
  };

  const renderTileLetter = () => {
    return <StyledTileLetter>{tileObj.letter}</StyledTileLetter>;
  };

  return (
    <div>
      {
        <StyledCenterTile
          pos_x={tileObj.pos_x}
          pos_y={tileObj.pos_y}
          angle={tileObj.angle}
          onClick={() => {
            sendFlipped();
          }}
        >
          {tileObj.is_flipped && renderTileLetter()}
        </StyledCenterTile>
      }
    </div>
  );
});

export default Tile;
