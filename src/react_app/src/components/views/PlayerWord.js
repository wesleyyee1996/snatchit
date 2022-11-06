import { observer } from 'mobx-react-lite';
import React from 'react';
import { StyledPlayerWord } from '../styles/PlayerWord.styled';
import Tile from './Tile';

const PlayerWord = observer(({gameStore, word}) => {

  function createWordTiles() {
    var letterArr = []
    for (let i in word) {
      letterArr.push(word[i]);
    }
    return letterArr;
  };

  return (
    <StyledPlayerWord width={word.length * 8}>
      {createWordTiles().map((letter) => <Tile gameStore={gameStore} letter={letter} inCenter={false}/>)}
    </StyledPlayerWord>
  );
});

export default PlayerWord;