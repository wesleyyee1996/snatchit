import { observer } from "mobx-react-lite";
import React from "react";
import { StyledPlayerWord } from "../../styles/PlayerWord.styled";
import PlayerTile from "./PlayerTile";

const PlayerWord = observer(({ gameStore, word }) => {
  function createWordTiles() {
    var letterArr = [];
    for (let i in word) {
      letterArr.push(word[i]);
    }
    return letterArr;
  }

  return (
    <div class="container mb-1">
      <StyledPlayerWord width={word.length * 8}>
        {createWordTiles().map((letter) => (
          <PlayerTile letter={letter} />
        ))}
      </StyledPlayerWord>
    </div>
  );
});

export default PlayerWord;
