import React from 'react';
import { StyledGameBoard } from './styles/GameBoard.styled';
import Tile from './Tile';

const tile_data = {
  a: 5,
  b: 2,
  c: 4,
  d: 4,
  e: 12,
  f: 4,
  g: 2,
  h: 5,
  i: 5,
  j: 1,
  k: 1,
  l: 5,
  m: 4,
  n: 5,
  o: 6,
  p: 3,
  q: 1,
  r: 5,
  s: 5,
  t: 7,
  u: 4,
  v: 2,
  w: 3,
  x: 1,
  y: 3,
  z: 1
}

const GameBoard = () => {

  function generateBoard() {
    var allTiles = [];
    for (var letter in tile_data) {
      for (let i=0; i <= tile_data[letter]; i++) {
        allTiles.push(
          <Tile letter = {letter} />
        )
      }
    }

    return allTiles.sort(() => Math.random() - 0.5);
  }
  
  
  return (
    <StyledGameBoard>
      {generateBoard().map((tile) => <div>{tile}</div>)}
    </StyledGameBoard>
  );
}

export default GameBoard;