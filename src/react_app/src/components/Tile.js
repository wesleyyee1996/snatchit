import React, {useState} from 'react'
import { StyledTile } from './styles/Tile.styled';
import { StyledTileLetter } from './styles/TileLetter.styled';
import { observer } from 'mobx-react-lite';
import axios from 'axios'

const Tile = observer(({gameStore, letter}) => {

  const [isFlipped, setIsFlipped] = useState(false);

  const sendFlipped = () => {
    if (isFlipped === true) {
      return;
    }
    gameStore.postTileFlipped(letter);
  }

  return (
    <StyledTile onClick={() => {sendFlipped(); 
      setIsFlipped(true);
    }}> 
      {isFlipped && (
          <StyledTileLetter> 
            {
              letter
            }
          </StyledTileLetter>
      )}
      
    </StyledTile>
  );
});

export default Tile;
    