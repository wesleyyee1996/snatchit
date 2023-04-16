import { observer } from "mobx-react-lite";
import React from "react";
import PlayerCard from "./PlayerCard";

const PlayerView = observer(({ playerStore }) => {
  return (
    <div class="container-fluid">
      {playerStore.getPlayersList().map((p) => (
        <div class="row flex-row mb-3">
          <PlayerCard key={p.id} player={p}></PlayerCard>
        </div>
      ))}
    </div>
  );
});

export default PlayerView;
