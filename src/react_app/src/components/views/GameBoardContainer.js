import { observer } from 'mobx-react-lite';
import React from 'react';
import Navbar from 'react-bootstrap/Navbar'
import GameBoard from './GameBoard';
import Sidebar from './Sidebar';
import styled from 'styled-components'
import PlayerStore from '../stores/PlayerStore';

const StyledGameBoardContainer = styled.div`
  height: 97vh;
  display: flex;
  flex-direction: row;
  gap: 1rem;
  background-color: green;
  bottom: 10%;
`

const GameBoardContainer = observer(({gameStore}) => {

  let playerStore = new PlayerStore();

  return(    
    <>
    <Navbar></Navbar>
    
    <div class="container-fluid">
      <div class="row">
        <div class="col-8">
          <StyledGameBoardContainer>
            <GameBoard gameStore={gameStore}/>
          </StyledGameBoardContainer>
        </div>
        <div class="col">
          <Sidebar gameStore={gameStore} playerStore={playerStore}/> 
        </div>
      </div>
      </div>
    </>
  )
});

export default GameBoardContainer;