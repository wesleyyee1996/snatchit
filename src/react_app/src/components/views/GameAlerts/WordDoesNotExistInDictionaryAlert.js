import { React } from "react";
import { observer } from "mobx-react-lite";
import Alert from "react-bootstrap/Alert";
import "../../styles/game_alert_styles.css";

const WordDoesNotExistInDictionaryAlert = observer(({ gameAlertStore }) => {
  if (!gameAlertStore.showWordDoesNotExistInDictionaryAlert) {
    return null;
  }
  return (
    <div style={{ position: "fixed", zIndex: 9999, top: "1%", left: "35%" }}>
      <Alert
        variant="warning"
        dismissible
        fade
        show
        text-center
        onClose={() =>
          (gameAlertStore.showWordDoesNotExistInDictionaryAlert = false)
        }
      >
        <strong>Uh oh!</strong>
        <p>{gameAlertStore.wordDoesNotExistInDictionaryMessage}</p>
      </Alert>
    </div>
  );
});

export default WordDoesNotExistInDictionaryAlert;
