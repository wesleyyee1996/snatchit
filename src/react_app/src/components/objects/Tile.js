import { makeAutoObservable } from "mobx";

class Tile {
  constructor(id, letter, inCenter, top_pos, left_pos, angle) {
    makeAutoObservable(this);
    this.id = id;
    this.letter = letter;
    this.inCenter = inCenter;
    this.top_pos = top_pos;
    this.left_pos = left_pos;
    this.angle = angle;
    this.isHidden = false;
    this.isFlipped = false;
  }

  setIsHidden() {
    this.isHidden = true;
  }

  setIsFlipped() {
    if (this.isFlipped === false) {
      this.isFlipped = true;
    }
  }

  setInCenter() {
    this.inCenter = false;
  }
}

export default Tile;
