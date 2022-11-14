import { observer } from 'mobx-react-lite';
import React from 'react';
import PlayerWord from './PlayerWord';

const PlayerView = observer(({playerStore, gameStore}) => {

  return (
    <div>
      <PlayerWord word={"hello"}/>
    </div>
  );
});

export default PlayerView;