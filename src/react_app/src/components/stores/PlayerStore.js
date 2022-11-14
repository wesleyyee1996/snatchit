import { makeAutoObservable } from "mobx";
import Player from "../objects/Player";


export default class PlayerStore {



  constructor() {
    makeAutoObservable(this)
    this.player = new Player();
  }
}