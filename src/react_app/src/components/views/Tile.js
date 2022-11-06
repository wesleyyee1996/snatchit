import React, {useState} from 'react'
import { StyledTile, StyledCenterTile, StyledPlayerTile } from '../styles/Tile.styled';
import { StyledTileLetter } from '../styles/TileLetter.styled';
import { observer } from 'mobx-react-lite';

const Tile = observer(({gameStore, letter, inCenter}) => {

  const [isFlipped, setIsFlipped] = useState(false);

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
            <StyledCenterTile onClick={() => {
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
    