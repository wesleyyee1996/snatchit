import { observer } from "mobx-react-lite";
import React from "react";
import Card from "react-bootstrap/Card";
import PlayerWord from "./PlayerWord";

const PlayerCard = observer(({ player }) => {
  const formPlayerName = (name) => {
    return (
      <div>
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

  return (
    <Card>
      <div class="container mb-3 mt-1">
        <div class="row text-center">{formPlayerName(player.name)}</div>
        <div class="row">{formPlayerWords(player)}</div>
      </div>
    </Card>
  );
});

export default PlayerCard;
