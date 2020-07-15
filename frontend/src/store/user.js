import { app } from '../plugins/app'

const state = {
  token: localStorage.getItem(app.constants.LOCAL_STORAGE_TOKEN),
  username: null,
}

// If state.token has initial value, send that value to axios instance
if (state.token) app.api.setToken(state.token)

export const mutations = {
  setUsername (state, username) {
    state.username = username
  },
  setToken (state, token) {
    state.token = token
    app.api.setToken(token)
    localStorage.setItem(app.constants.LOCAL_STORAGE_TOKEN, token)
  },
}

const actions = {
  login ({ commit }, { username, password }) {
    return new Promise((resolve, reject) => {
      app.api.login({ username, password }).then(result => {
        const token = result.data.access
        commit('setToken', token)
        commit('setUsername', username)
        resolve()
      }).catch(error => reject(error))
    })
  },
  logout ({ commit }) {
    return new Promise((resolve, reject) => {
      app.api.logout().then(() => {
        commit('setToken', null)
        commit('setUsername', null)
        resolve()
      }).catch(error => reject(error))
    })
  },
  register ({ commit }, { username, password }) {
    return new Promise((resolve, reject) => {
      app.api.register({ username, password }).then(result => {
        const token = result.data.access
        commit('setToken', token)
        commit('setUsername', username)
        resolve()
      }).catch(error => reject(error))
    })
  },
  loadUser ({ commit }) {
    return new Promise((resolve, reject) => {
      app.api.user().then(result => {
        commit('setUsername', result.data.username)
        resolve()
      }).catch(error => reject(error))
    })
  },
}

export default {
  namespaced: true,
  state,
  mutations,
  actions,
}
