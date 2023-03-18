import { observer } from 'mobx-react-lite';
import React from 'react';
import PlayerWord from './PlayerWord';

const PlayerView = observer(({playerStore, gameStore}) => {

  const formPlayerName = (name) => {
    return <h3>
      {name}
    </h3>
  }

  const formPlayerWords = (player) => {
    return player.words.map((w) => (
      <div class="row">
        <PlayerWord word={w}></PlayerWord>
      </div>
    ));
  }

  return (
    <div class="container-fluid">
      {
        playerStore.players.map((p) => (
            <div class="row">
              <div class="row text-center">
                {formPlayerName(p.name)}
              </div>
              <div class="row">
                {formPlayerWords(p)}
              </div>
            </div>
          )
        )
      }
    </div>
  );
});

export default PlayerView;