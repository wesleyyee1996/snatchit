import { observer } from 'mobx-react-lite';
import React from 'react';
import { StyledGameBoardContainer } from '../styles/GameBoardContainer.styled';

import GameBoard from './GameBoard';
import NewGame from './NewGame';
import Sidebar from './Sidebar';
import WordForm from './WordForm';
import PlayerStore from '../stores/PlayerStore';
import PlayersContainer from './PlayersContainer';

const GameBoardContainer = observer(({gameStore}) => {

  let playerStore = new PlayerStore();

  return(    
    <>
      <StyledGameBoardContainer>
        <Sidebar gameStore={gameStore}/>
        <GameBoard gameStore={gameStore}/>
        <WordForm gameStore={gameStore}/> 
        <NewGame gameStore={gameStore}/>        
      </StyledGameBoardContainer>
      {/* <PlayersContainer playerStore={playerStore} gameStore={gameStore}/> */}
    </>
  )
});

export default GameBoardContainer;