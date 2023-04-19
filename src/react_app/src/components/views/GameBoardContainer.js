import { observer } from "mobx-react-lite";
import React from "react";
import Navbar from "react-bootstrap/Navbar";
import GameBoard from "./GameBoard";
import Sidebar from "./Sidebar";
import styled from "styled-components";
import NewGameModal from "./NewGame/NewGameModal";
import GameAlerts from "./GameAlerts/GameAlerts";

const StyledGameBoardContainer = styled.div`
  height: 97vh;
  display: flex;
  flex-direction: row;
  gap: 1rem;
  bottom: 10%;
`;

const GameBoardContainer = observer(({ gameStore }) => {
  return (
    <>
      <Navbar></Navbar>
      <NewGameModal
        newGameModalStore={gameStore.newGameModalStore}
        playerStore={gameStore.playerStore}
      />
      <GameAlerts gameAlertStore={gameStore.gameAlertsStore}></GameAlerts>

      <div class="container-fluid">
        <div class="row">
          <div class="col-8">
            <StyledGameBoardContainer>
              <GameBoard gameStore={gameStore} />
            </StyledGameBoardContainer>
          </div>
          <div class="col">
            <div class="container-fluid rounded">
              <Sidebar gameStore={gameStore} />
            </div>
          </div>
        </div>
      </div>
    </>
  );
});

export default GameBoardContainer;
