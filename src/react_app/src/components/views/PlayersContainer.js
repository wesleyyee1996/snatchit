import { observer } from 'mobx-react-lite';
import React from 'react';
import PlayerWord from './PlayerWord';

const PlayersContainer = observer(({playerStore, gameStore}) => {

  return (
    <div>
      <PlayerWord word={"helloasdf"}/>
    </div>
  );
});

export default PlayersContainer;