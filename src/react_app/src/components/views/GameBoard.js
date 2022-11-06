import React from 'react';
import { StyledGameBoard } from '../styles/GameBoard.styled';
import Tile from './Tile';
import { useEffect, useState } from 'react';
import { observer } from 'mobx-react-lite';

const GameBoard = observer(({gameStore}) => {

  const [tiles, setTiles] = useState([]);

  function generateBoard() {
    var allTiles = [];
    for (var letter in gameStore.letterJsonData) {
      for (let i=0; i <= gameStore.letterJsonData[letter]; i++) {
        allTiles.push(
          <Tile letter = {letter} gameStore = {gameStore} />
        )
      }
    }

    const shuffledTiles = allTiles.sort(() => Math.random() - 0.5);
    setTiles(shuffledTiles);
  }

  useEffect(() => {
    gameStore.getLetterData();
  }, []);

  useEffect(() => {
    generateBoard();
  }, [gameStore.letterJsonData])
  
  return (
    <>
      <StyledGameBoard>
        {tiles.map((tile) => <div>{tile}</div>)}
      </StyledGameBoard>
    </>
  );
});

export default GameBoard;