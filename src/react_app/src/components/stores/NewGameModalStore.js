import { makeAutoObservable } from "mobx";

export default class NewGameModalStore {
  showModal = true;
  usernameError = false;
  showRegisterUserForm = true;

  constructor(gameStore) {
    makeAutoObservable(this);
    this.gameStore = gameStore;
  }

  startGame() {
    if (this.gameStore.playerStore.numPlayers() > 0) {
      this.showModal = false;
    }
  }

  addPlayer(username) {
    if (username === "") {
      this.usernameError = true;
      return;
    }
    this.gameStore.getAddNewPlayer(username);
    this.showRegisterUserForm = false;
  }
}
