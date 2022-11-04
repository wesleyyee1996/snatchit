import React, {useState} from 'react'
import { StyledTile } from './styles/Tile.styled';
import { StyledTileLetter } from './styles/TileLetter.styled';
import axios from 'axios'

const Tile = (props) => {
  const [isFlipped, setIsFlipped] = useState(false);

  const sendFlipped = () => {
    if (isFlipped === true) {
      return;
    }
    axios.post('http://127.0.0.1:8000/api/tile/'+props.letter).then(
      res => {
        console.log(res);
      }).catch(
      error => {
        console.log(error)
    });
  }

  return (
    <StyledTile onClick={() => {sendFlipped(); 
      setIsFlipped(true);
    }}> 
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
    