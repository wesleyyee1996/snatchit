import React, { useState } from "react";
import { observer } from "mobx-react-lite";

const WordForm = observer(({ gameStore }) => {
  const [wordText, setWordText] = useState("");

  const submitWord = (e) => {
    e.preventDefault();
    const playerId = gameStore.playerStore.getCurrentPlayer();
    gameStore.getSubmitWord(wordText, playerId);
    setWordText("");
  };

  return (
    <form>
      <div class="row g-3 align-items-center">
        <div class="row">
          <div class="col-auto">
            <label class="form-label">Word: </label>
          </div>
          <div class="col-auto">
            <input
              class="form-control"
              type="text"
              value={wordText}
              onChange={(e) => {
                setWordText(e.target.value);
              }}
            />
          </div>
          <div class="col-auto">
            <button class="btn btn-primary" onClick={(e) => submitWord(e)}>
              {" "}
              Submit
            </button>
          </div>
        </div>
      </div>
    </form>
  );
});

export default WordForm;
