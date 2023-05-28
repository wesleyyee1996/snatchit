import React, { useState } from "react";
import { StyledPlayerTile } from "../../styles/Tile.styled";
import { observer } from "mobx-react-lite";

const PlayerTile = observer(({ letter }) => {

  return (
    <div>
      {
        <StyledPlayerTile>{letter}</StyledPlayerTile>
      }
    </div>
  );
});

export default PlayerTile;