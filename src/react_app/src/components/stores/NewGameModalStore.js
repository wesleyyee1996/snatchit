import { makeAutoObservable, computed } from "mobx";

export default class NewGameModalStore {
  showModal = true;
  usernameError = false;
  showRegisterUserForm = true;

  constructor(gameStore) {
    makeAutoObservable(this, {
      disableStartGameButton: computed,
    });
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

  get disableStartGameButton() {
    return this.gameStore.playerStore.numPlayers() < 2;
  }
}
