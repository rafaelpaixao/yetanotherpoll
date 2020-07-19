import axios from 'axios'
import { tokenStorage } from './storage'

const URLS = {
  LOGIN: 'login/',
  REGISTER: 'register/',
}

class Api {
  constructor () {
    this.axios = axios.create()
  }

  addResponseInterceptors ({ success = null, error = null }) {
    this.axios.interceptors.response.use(
      success,
      error,
    )
  }

  setBaseUrl (baseURL) {
    this.axios.defaults.baseURL = baseURL
  }

  useToken (token) {
    if (token) {
      this.token = token
      this.axios.defaults.headers.common = {
        Authorization: 'Bearer ' + token
      }
      tokenStorage.set(token)
    } else {
      this.logout()
    }
  }

  logout () {
    this.axios.defaults.headers.common = {}
    this.token = null
    tokenStorage.delete()
  }

  login (data) {
    return this.axios.post(URLS.LOGIN, data)
  }

  register (data) {
    return this.axios.post(URLS.REGISTER, data)
  }
}

export default new Api()
