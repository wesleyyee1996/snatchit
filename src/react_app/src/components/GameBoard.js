import React from 'react';
import { StyledGameBoard } from './styles/GameBoard.styled';
import WordForm from './WordForm';
import Tile from './Tile';
import axios from 'axios'
import { useEffect, useState } from 'react';

const GameBoard = () => {

  const [letterCounts, setLetterCounts] = useState('');

  const [tiles, setTiles] = useState([]);

  function generateBoard() {
    var allTiles = [];
    for (var letter in letterCounts) {
      for (let i=0; i <= letterCounts[letter]; i++) {
        allTiles.push(
          <Tile letter = {letter} />
        )
      }
    }

    const shuffledTiles = allTiles.sort(() => Math.random() - 0.5);
    setTiles(shuffledTiles);
  }

  useEffect(() => {
    async function fetchData() {
      const req = await axios.get('http://127.0.0.1:8000/api/generateBoard')
      setLetterCounts(req.data)
    }
    fetchData();
  }, []);

  useEffect(() => {
    generateBoard();
  }, [letterCounts])
  
  return (
    <>
      <StyledGameBoard>
        {tiles.map((tile) => <div>{tile}</div>)}
      </StyledGameBoard>
      <WordForm/>
    </>
  );
}

export default GameBoard;