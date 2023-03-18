import React from 'react';
import styled from 'styled-components'
import WordForm from './WordForm';
import PlayerView from './PlayerView';

const StyledSidebar = styled.div`
  // display: flex;
  align-items: center;
  justify-content: center;
  height: 98vh;
  // flex-grow: 1;
  // margin: 2vh;
  background-color: white;
`

const Sidebar = ({gameStore}) => {

  return (
    <StyledSidebar>
      <div class="container p-1">
        <div class="row p-1">
          <WordForm gameStore={gameStore}/> 
        </div>
        <div class="row p-1">
          <form>
            <button class="btn btn-primary" onClick={gameStore.getNewGame()}>New Game</button>
          </form>
        </div>
        <div class="row p-1">
          <PlayerView playerStore={gameStore.playerStore}></PlayerView>
        </div>
      
    </div>
    </StyledSidebar>
  );
};

export default Sidebar;