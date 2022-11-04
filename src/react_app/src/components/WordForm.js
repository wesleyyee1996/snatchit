import React, {useState} from 'react'
import axios from 'axios'

const WordForm = () => {

  const [wordText, setWordText] = useState('');

  const submitWord = () => {
    const response = axios.get('http://127.0.0.1:8000/api/word/'+wordText).then(
      res => {
        console.log(res);
      }).catch(
      error => {
        console.log(error);
    console.log(response)
  });
  }
  
  return(
    <form>
      <label>Word: </label>
      <input type='text' value={wordText} onChange={(e)=>{setWordText(e.target.value)}}/>
      <button onClick={submitWord}> Submit</button>
    </form>
  );
};

export default WordForm;