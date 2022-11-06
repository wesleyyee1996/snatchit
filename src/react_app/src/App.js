import logo from './logo.svg';
import './App.css';
import React from 'react';
import GameBoardContainer from './components/views/GameBoardContainer';
import { GameStore } from './components/stores/GameStore';

function App() {
  return (
    <div className="App">
        <GameBoardContainer gameStore = {GameStore}/>
    </div>
  );
}

export default App;
