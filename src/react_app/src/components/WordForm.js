import React, {useState} from 'react'
import axios from 'axios'
import { observer } from 'mobx-react-lite';

const WordForm = observer(({gameStore}) => {

  const [wordText, setWordText] = useState('');

  const submitWord = (e) => {
    e.preventDefault();
    gameStore.getSubmitWord(wordText);
    setWordText('');
  }
  
  return(
    <form>
      <label>Word: </label>
      <input type='text' value={wordText} onChange={(e)=>{setWordText(e.target.value)}}/>
      <button onClick={(e) => submitWord(e)}> Submit</button>
    </form>
  );
});

export default WordForm;