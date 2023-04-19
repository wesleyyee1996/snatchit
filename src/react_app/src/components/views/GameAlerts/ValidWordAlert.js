import { React } from "react";
import { observer } from "mobx-react-lite";
import Alert from "react-bootstrap/Alert";
import "../../styles/game_alert_styles.css";

const ValidWordAlert = observer(({ gameAlertStore }) => {
  if (!gameAlertStore.showValidWordAlert) {
    return null;
  }
  return (
    <div style={{ position: "fixed", zIndex: 9999, top: "1%", left: "35%" }}>
      <Alert
        variant="info"
        dismissible
        fade
        show
        text-center
        onClose={() => (gameAlertStore.showValidWordAlert = false)}
      >
        <strong>Noice!!</strong>
        <p>{gameAlertStore.validWordAlertMessage}</p>
      </Alert>
    </div>
  );
});

export default ValidWordAlert;
