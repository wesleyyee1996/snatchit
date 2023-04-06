import React, { useState } from "react";
import {
  StyledTile,
  StyledCenterTile,
  StyledPlayerTile,
} from "../styles/Tile.styled";
import { StyledTileLetter } from "../styles/TileLetter.styled";
import { observer } from "mobx-react-lite";

const Tile = observer(({ gameStore, tileObj }) => {
  const [isFlipped, setIsFlipped] = useState(false);

  const sendFlipped = () => {
    if (tileObj.isFlipped === true) {
      return;
    }
    gameStore.postTileFlipped(tileObj.id);
    tileObj.setIsFlipped();
    setIsFlipped(true);
  };

  const renderTileLetter = () => {
    return <StyledTileLetter>{tileObj.letter}</StyledTileLetter>;
  };

  return (
    <div>
      {tileObj.inCenter && (
        <StyledCenterTile
          top_pos={tileObj.top_pos}
          left_pos={tileObj.left_pos}
          angle={tileObj.angle}
          onClick={() => {
            sendFlipped();
          }}
        >
          {tileObj.isFlipped && renderTileLetter()}
        </StyledCenterTile>
      )}
      {/* {!tileObj.inCenter && (
        <StyledPlayerTile>{renderTileLetter()}</StyledPlayerTile>
      )} */}
    </div>
  );
});

export default Tile;
