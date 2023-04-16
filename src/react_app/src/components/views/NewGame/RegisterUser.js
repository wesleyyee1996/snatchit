import React, { useState } from "react";
import { observer, action } from "mobx-react-lite";
import { Button, Form } from "react-bootstrap";

const RegisterUserForm = observer(({ newGameModalStore }) => {
  const [playerName, setPlayerName] = useState("");

  const handleKeyPress = (event) => {
    if (event.key === "Enter") {
      event.preventDefault();
      event.stopPropagation();
      newGameModalStore.addPlayer(playerName);
    }
  };

  return (
    <Form>
      <Form.Group controlId="formText">
        <Form.Label>Enter your username: </Form.Label>
        <Form.Control
          type="text"
          onChange={(e) => {
            setPlayerName(e.target.value);
          }}
          isInvalid={newGameModalStore.usernameError}
          onKeyDown={handleKeyPress}
        />
        <Form.Control.Feedback type="invalid">
          Please enter a username!
        </Form.Control.Feedback>
      </Form.Group>
      <Button
        type="button"
        variant="primary"
        onClick={(e) => {
          e.preventDefault();
          newGameModalStore.addPlayer(playerName);
        }}
      >
        Submit
      </Button>
    </Form>
  );
});

export default RegisterUserForm;
