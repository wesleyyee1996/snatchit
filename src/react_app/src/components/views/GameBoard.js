import React from 'react';
import { StyledGameBoard } from '../styles/GameBoard.styled';
import Tile from './Tile';
import { useEffect, useState } from 'react';
import { observer } from 'mobx-react-lite';
import { getRandomNumberBetween } from '../../helpers';

const GameBoard = observer(({gameStore}) => {

  const [tiles, setTiles] = useState([]);

  function generateBoard() {
    var allTiles = [];
    console.log(gameStore.tileData)
    gameStore.tileData.forEach(
      tile => (
        allTiles.push(
          <Tile letter = {tile['letter']} gameStore = {gameStore} inCenter={true} top_pos={tile['pos_x']} left_pos={tile['pos_y']} angle={tile['angle']}/>
        )
      )
    )

    const shuffledTiles = allTiles.sort(() => Math.random() - 0.5);
    setTiles(shuffledTiles);
  }

  useEffect(() => {
    gameStore.getLetterData();
  }, []);

  useEffect(() => {
    generateBoard();
  }, [gameStore.tileData])
  
  return (
    <>
      <StyledGameBoard>
        {tiles.map((tile) => <div>{tile}</div>)}
      </StyledGameBoard>
    </>
  );
});

export default GameBoard;