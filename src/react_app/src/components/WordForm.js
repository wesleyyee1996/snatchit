import React, {useState} from 'react'
import axios from 'axios'

const WordForm = () => {

  const [wordText, setWordText] = useState('');

  const submitWord = (e) => {
    e.preventDefault();
    axios.get('http://127.0.0.1:8000/api/word/'+wordText).then(
      res => {
        console.log(res);
      }).catch(
      error => {
        console.log(error);
      }
    );
    setWordText('');
  }
  
  return(
    <form>
      <label>Word: </label>
      <input type='text' value={wordText} onChange={(e)=>{setWordText(e.target.value)}}/>
      <button onClick={(e) => submitWord(e)}> Submit</button>
    </form>
  );
};

export default WordForm;