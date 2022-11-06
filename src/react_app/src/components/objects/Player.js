class Player {

  words = [];
  points = 0;

  constructor (name) {
    this.name = name
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