import React, {useState} from 'react'
import { StyledTile } from './styles/Tile.styled';
import { StyledTileLetter } from './styles/TileLetter.styled';

const Tile = (props) => {
  const [isFlipped, setIsFlipped] = useState(false);

  return (
    <StyledTile onClick={() => setIsFlipped(!isFlipped)}> 
      {isFlipped && (
          <StyledTileLetter> 
            {
              props.letter
            }
          </StyledTileLetter>
      )}
      
    </StyledTile>
  );
}

export default Tile;
    