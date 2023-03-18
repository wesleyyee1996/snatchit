import React from 'react';
import styled from 'styled-components'
import NewGame from './NewGame';
import WordForm from './WordForm';
import PlayerView from './PlayerView';

const StyledSidebar = styled.div`
  // display: flex;
  align-items: center;
  justify-content: center;
  // height: 100%;
  // flex-grow: 1;
  // margin: 2vh;
  background-color: red;
`

const Sidebar = ({gameStore, playerStore}) => {

  return (
    <div class="container-fluid p-1">
      <StyledSidebar>
        <div class="row p-1">
          <WordForm gameStore={gameStore}/> 
        </div>
        <div class="row p-1">
          <NewGame gameStore={gameStore}/>
        </div>
        <div class="row p-1">
          <PlayerView playerStore={playerStore}></PlayerView>
        </div>
        
        
      </StyledSidebar>
    </div>
  );
};

export default Sidebar;