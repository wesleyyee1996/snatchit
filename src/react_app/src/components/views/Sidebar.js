import React from 'react';
import { StyledSidebar } from '../styles/Sidebar.styled';
import PlayerWord from './PlayerWord';
import PlayerView from './PlayerView';
import PlayerStore from '../stores/PlayerStore';

const Sidebar = ({gameStore}) => {

  let playerStore = new PlayerStore;

  return (
    <div>
      <StyledSidebar>
        <PlayerView playerStore={playerStore} gameStore={gameStore}/>
      </StyledSidebar>
    </div>
  );
};

export default Sidebar;