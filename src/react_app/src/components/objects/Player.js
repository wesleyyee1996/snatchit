import { makeAutoObservable } from "mobx";

class Player {
  words = [];
  points = 0;

  constructor(name) {
    makeAutoObservable(this);
    this.name = name;
    this.id = 1;
  }

  addWord(word) {
    this.words.push(word);
    this.points += word.length;
  }

  removeWord(word) {
    this.words.splice(this.words.indexOf(word), 1);
    this.points -= word.length;
  }
}

export default Player;
