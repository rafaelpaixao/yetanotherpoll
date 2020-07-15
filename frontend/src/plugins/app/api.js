import axios from 'axios'

const URLS = {
  LOGIN: 'token/',
  REGISTER: 'register/',
  USER: 'user/me/',
}

class Api {
  constructor () {
    this.axios = axios.create()
  }

  setBaseUrl (baseURL) {
    this.axios.defaults.baseURL = baseURL
  }

  setToken (token) {
    this.axios.defaults.headers.common = {
      Authorization: 'Bearer ' + token
    }
  }

  logout () {
    return new Promise((resolve, reject) => {
      this.axios.defaults.headers.common = {}
      resolve()
    })
  }

  login (data) {
    return this.axios.post(URLS.LOGIN, data)
  }

  register (data) {
    return this.axios.post(URLS.REGISTER, data)
  }

  getUser () {
    return this.axios.get(URLS.USER)
  }
}

export default new Api()
