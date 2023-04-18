import React from "react";
import { observer } from "mobx-react-lite";
import { Modal, Button, Popover } from "react-bootstrap";
import RegisterUserForm from "./RegisterUser";
import NewPlayerCard from "./NewPlayerCard";

const NewGameModal = observer(({ newGameModalStore, playerStore }) => {
  const renderRegisterUserForm = () => {
    if (newGameModalStore.showRegisterUserForm) {
      return (
        <RegisterUserForm
          newGameModalStore={newGameModalStore}
        ></RegisterUserForm>
      );
    }
  };

  const renderUsers = () => {
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
  };

  return (
    <Modal show={newGameModalStore.showModal} centered backdrop="static">
      <Modal.Header>
        <Modal.Title>Start a New Game</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <div class="container">{renderUsers()}</div>
        <div class="container">{renderRegisterUserForm()}</div>
      </Modal.Body>
      <Modal.Footer>
        <span
          class="d-inline-block"
          data-toggle="popover"
          data-trigger="hover"
          data-content="Disabled popover"
        >
          <Button
            variant="primary"
            onClick={(e) => {
              newGameModalStore.startGame();
              e.preventDefault();
            }}
            disabled={newGameModalStore.disableStartGameButton}
          >
            Start New Game
          </Button>
        </span>
      </Modal.Footer>
    </Modal>
  );
});

export default NewGameModal;
