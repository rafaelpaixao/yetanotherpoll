import axios from 'axios'
import { tokenStorage } from './storage'

const URLS = {
  LOGIN: 'login/',
  REGISTER: 'register/',
  REGISTER_GUEST: 'register_guest/',
  POLL_LIST: 'poll/',
  POLL_CREATE: 'poll/create/',
  POLL: id => `poll/${id}/`,
  POLL_EDIT: id => `poll/${id}/edit`,
  POLL_RESULTS: id => `poll/${id}?results=true`,
  VOTE: id => `vote/${id}/`,
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

  registerGuest (data) {
    return this.axios.post(URLS.REGISTER_GUEST, data)
  }

  createPoll (data) {
    return this.axios.post(URLS.POLL_CREATE, data)
  }

  fetchPoll (id) {
    return this.axios.get(URLS.POLL(id))
  }

  fetchPollWithResults (id) {
    return this.axios.get(URLS.POLL_RESULTS(id))
  }

  fetchUserPolls () {
    return this.axios.get(URLS.POLL_LIST)
  }

  _createPoll (data) {
    return this.axios.post(URLS.POLL_CREATE, data)
  }

  _editPoll (data) {
    return this.axios.post(URLS.POLL_EDIT(data.id), data)
  }

  submitPoll (data) {
    return data.id ? this._editPoll(data) : this._createPoll(data)
  }

  submitVote (optionId) {
    return this.axios.post(URLS.VOTE(optionId))
  }
}

export default new Api()
