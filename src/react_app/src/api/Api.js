import axios from 'axios'

class Api {
  getLetterData() {
    async function fetchData() {
      const req = await axios.get('http://127.0.0.1:8000/api/generateBoard');
      return req.data;
    }
    let letterJsonData;
    fetchData().then(data => letterJsonData = data);
    console.log('test', letterJsonData)
    return letterJsonData;
  }
}

export default Api;