import React from 'react';
import { StyledSidebar } from '../styles/Sidebar.styled';
import PlayerWord from './PlayerWord';

const Sidebar = ({gameStore}) => {
  return (
    <div>
      <StyledSidebar>
        <PlayerWord word={"test"}/>
      </StyledSidebar>
    </div>
  );
};

export default Sidebar;