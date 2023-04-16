import React from "react";
import { observer } from "mobx-react-lite";
import { Card } from "react-bootstrap";

const NewPlayerCard = observer(({ playerObj }) => {
  if (playerObj !== undefined) {
    return <Card>{playerObj.name}</Card>;
  }
});

export default NewPlayerCard;
