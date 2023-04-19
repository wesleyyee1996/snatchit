import { makeAutoObservable } from "mobx";

export default class GameAlertsStore {
  showWordDoesNotExistInDictionaryAlert = false;
  wordDoesNotExistInDictionaryMessage = "";

  showWordIsTooShortAlert = false;
  wordIsTooShortMessage = "";

  showCannotMakeWordFromGameTilesAlert = false;

  showValidWordAlert = false;
  validWordAlertMessage = "";

  constructor(gameStore) {
    makeAutoObservable(this);
    this.gameStore = gameStore;
  }

  addWordIsTooShortAlert(message) {
    this.showWordIsTooShortAlert = true;
    this.wordIsTooShortMessage = message;
  }

  addWordDoesNotExistInDictionaryAlert(message) {
    this.showWordDoesNotExistInDictionaryAlert = true;
    this.wordDoesNotExistInDictionaryMessage = message;
  }

  setValidWordAlert(message) {
    this.showValidWordAlert = true;
    this.validWordAlertMessage = message;
  }
}
