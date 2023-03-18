import React, {useState} from 'react'
import { StyledTile, StyledCenterTile, StyledPlayerTile } from '../styles/Tile.styled';
import { StyledTileLetter } from '../styles/TileLetter.styled';
import { observer } from 'mobx-react-lite';

const Tile = observer(({gameStore, id, letter, inCenter, top_pos, left_pos, angle}) => {

  const [isFlipped, setIsFlipped] = useState(false);

  const [isHidden, setIsHidden] = useState(false);

  const sendFlipped = () => {
    if (isFlipped === true) {
      return;
    }
    gameStore.postTileFlipped(letter);
    setIsFlipped(true);
  }

  const renderTileLetter = () => {
    return (
      (
        <StyledTileLetter> 
          {
            letter
          }
        </StyledTileLetter>
    ))
  };

  return (
    <div>
        {
          inCenter && (
            <StyledCenterTile top_pos = {top_pos} left_pos = {left_pos} angle={angle}
              onClick={() => {
              sendFlipped(); 
            }}> 
              {isFlipped && renderTileLetter()}      
            </StyledCenterTile>
          )
        }
        {
          !inCenter && (
            <StyledPlayerTile> 
              {renderTileLetter()}      
            </StyledPlayerTile>
          )
        }
    </div>
  );
});

export default Tile;
    