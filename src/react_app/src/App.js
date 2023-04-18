import logo from "./logo.svg";
import "./App.css";
import React from "react";
import GameBoardContainer from "./components/views/GameBoardContainer";
import { GameStore } from "./components/stores/GameStore";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";

function App() {
  return (
    <div className="App">
      <GameBoardContainer gameStore={GameStore} />
    </div>
  );
}

export default App;
