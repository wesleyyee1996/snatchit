import { makeAutoObservable } from "mobx";

class Player {
  words = [];
  points = 0;

  constructor(id, name = "") {
    makeAutoObservable(this);
    this.name = name;
    this.id = id;
  }

  addWord(word) {
    if (!this.words.includes(word)) {
      this.words.push(word);
      this.points += word.length;
    }
  }

  removeWord(word) {
    if (this.words.includes(word)) {
      this.words.splice(this.words.indexOf(word), 1);
      this.points -= word.length;
    }
  }

  updateWords(new_words) {
    this.words = [];
    for (const word in new_words) {
      this.addWord(word);
    }
  }
}

export default Player;
