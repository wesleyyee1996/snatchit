import { observer } from 'mobx-react-lite';
import React from 'react';
import { StyledGameBoardContainer } from '../styles/GameBoardContainer.styled';

import GameBoard from './GameBoard';
import NewGame from './NewGame';
import Sidebar from './Sidebar';
import WordForm from './WordForm';

const GameBoardContainer = observer(({gameStore}) => {

  return(    
    <>
      <StyledGameBoardContainer>
        <Sidebar gameStore={gameStore}/>
        <GameBoard gameStore={gameStore}/>
        <WordForm gameStore={gameStore}/> 
        <NewGame gameStore={gameStore}/>        
      </StyledGameBoardContainer>
    </>
  )
});

export default GameBoardContainer;