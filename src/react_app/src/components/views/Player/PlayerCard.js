import { observer } from "mobx-react-lite";
import React from "react";
import Card from "react-bootstrap/Card";
import PlayerWord from "./PlayerWord";

const PlayerCard = observer(({ player }) => {
  const formPlayerName = (name) => {
    return (
      <div class="container" style={{ color: "#fdf6e3" }}>
        <h3>
          <strong>Player: </strong>
          <small>{name}</small>
        </h3>
      </div>
    );
  };

  const formPlayerWords = (p) => {
    return p.words.map((w) => (
      <div class="row">
        <PlayerWord word={w}></PlayerWord>
      </div>
    ));
  };

  const formPlayerPoints = (points) => {
    return (
        <div style={{ color: "#fdf6e3" }}>
          <h5>
            <strong>Pts: </strong>
            <small>{points}</small>
          </h5>
        </div>
    );
  };

  return (
    <div class="container">
      <Card style={{ backgroundColor: "#a3946d" }}>
        <div class="container mb-3 mt-1">
          <div class="row">
            <div class="col text-left">{formPlayerName(player.name)}</div>
            <div class="col text-end mt-2">{formPlayerPoints(player.points)}</div>
          </div>          
          <div class="row">{formPlayerWords(player)}</div>
        </div>
      </Card>
    </div>
  );
});

export default PlayerCard;
