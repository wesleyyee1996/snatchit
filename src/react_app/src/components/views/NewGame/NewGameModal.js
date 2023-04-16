import React from "react";
import { observer } from "mobx-react-lite";
import { Modal, Button } from "react-bootstrap";
import RegisterUserForm from "./RegisterUser";
import NewPlayerCard from "./NewPlayerCard";

const NewGameModal = observer(({ newGameModalStore, playerStore }) => {
  const renderUsers = () => {
    if (newGameModalStore.showRegisterUserForm) {
      return (
        <RegisterUserForm
          newGameModalStore={newGameModalStore}
        ></RegisterUserForm>
      );
    } else {
      const playersList = playerStore.getPlayersList();
      return (
        <div class="container">
          {playersList.length > 0 &&
            playersList.map((playerObj) => {
              return (
                <div>
                  <NewPlayerCard playerObj={playerObj}></NewPlayerCard>
                </div>
              );
            })}
        </div>
      );
    }
  };

  return (
    <Modal show={newGameModalStore.showModal} centered backdrop="static">
      <Modal.Header>
        <Modal.Title>Start a New Game</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <div class="container">{renderUsers()}</div>
      </Modal.Body>
      <Modal.Footer>
        <Button
          variant="primary"
          onClick={(e) => {
            newGameModalStore.startGame();
            e.preventDefault();
          }}
        >
          Start New Game
        </Button>
      </Modal.Footer>
    </Modal>
  );
});

export default NewGameModal;
