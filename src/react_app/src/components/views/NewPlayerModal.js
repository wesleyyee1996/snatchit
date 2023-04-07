import React, { useState } from "react";
import { observer } from "mobx-react-lite";
import { Modal, Button, Form } from "react-bootstrap";

const NewPlayerModal = observer(({ gameStore }) => {
  const [showModal, setShowModal] = useState(true);

  const [playerName, setPlayerName] = useState("");

  const [formError, setFormError] = useState(false);

  const handleClose = () => setShowModal(false);

  const handleSubmit = (e) => {
    e.preventDefault();

    if (playerName === "") {
      setFormError(true);
      return;
    }
    gameStore.getAddNewPlayer(playerName);
    setShowModal(false);
  };

  const handleKeyPress = (event) => {
    if (event.key === "Enter") {
      event.preventDefault();
      event.stopPropagation();
      handleSubmit(event);
    }
  };

  return (
    <Modal show={showModal} onHide={handleClose} centered backdrop="static">
      <Modal.Header>
        <Modal.Title>What's your name?</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <Form>
          <Form.Group controlId="formText">
            <Form.Label>Name</Form.Label>
            <Form.Control
              type="text"
              placeholder="hehe :)"
              onChange={(e) => {
                setPlayerName(e.target.value);
              }}
              isInvalid={formError}
              onKeyDown={handleKeyPress}
            />
            <Form.Control.Feedback type="invalid">
              Please enter a username!
            </Form.Control.Feedback>
          </Form.Group>
        </Form>
      </Modal.Body>
      <Modal.Footer>
        <Button variant="primary" onClick={handleSubmit}>
          Submit
        </Button>
      </Modal.Footer>
    </Modal>
  );
});

export default NewPlayerModal;
