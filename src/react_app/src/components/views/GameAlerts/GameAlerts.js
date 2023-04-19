import React from "react";
import { observer } from "mobx-react-lite";
import WordDoesNotExistInDictionaryAlert from "./WordDoesNotExistInDictionaryAlert";
import WordIsTooShortAlert from "./WordIsTooShortAlert";
import CannotMakeWordFromGameTilesAlert from "./CannotMakeWordFromGameTilesAlert";
import ValidWordAlert from "./ValidWordAlert";

const GameAlerts = observer(({ gameAlertStore }) => {
  return (
    <>
      <ValidWordAlert gameAlertStore={gameAlertStore}></ValidWordAlert>
      <WordDoesNotExistInDictionaryAlert
        gameAlertStore={gameAlertStore}
      ></WordDoesNotExistInDictionaryAlert>
      <WordIsTooShortAlert
        gameAlertStore={gameAlertStore}
      ></WordIsTooShortAlert>
      <CannotMakeWordFromGameTilesAlert
        gameAlertStore={gameAlertStore}
      ></CannotMakeWordFromGameTilesAlert>
    </>
  );
});

export default GameAlerts;
