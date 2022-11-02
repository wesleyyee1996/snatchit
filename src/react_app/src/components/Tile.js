import React, {useState} from 'react'
import { StyledTile } from './styles/Tile.styled';

export default function Tile(props) {
  const [isFlipped, setIsFlipped] = useState(false);

  return (
    <StyledTile onClick={() => setIsFlipped(!isFlipped)}> 
      <p> 
        {isFlipped ? 
          (props.letter) : (' ')
        }
      </p>
    </StyledTile>
  );
}
    