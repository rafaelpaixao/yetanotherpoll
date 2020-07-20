import { app } from '../plugins/app'
import router from '../router'

const state = {
  isGuest: false,
  userId: null,
  username: null,
}

const parseJwt = token => JSON.parse(atob(token.split('.')[1]))

export const mutations = {
  setUser (state, { isGuest, username, userId }) {
    state.isGuest = isGuest
    state.userId = userId
    state.username = username
  },
  unsetUser (state) {
    state.isGuest = false
    state.userId = null
    state.username = null
  },
}

const actions = {
  login ({ dispatch }, { username, password }) {
    return new Promise((resolve, reject) => {
      app.api.login({ username, password }).then(data => {
        dispatch('useToken', data.access)
        resolve()
      }).catch(error => reject(error))
    })
  },
  register ({ dispatch }, { username, password }) {
    return new Promise((resolve, reject) => {
      app.api.register({ username, password }).then(data => {
        dispatch('useToken', data.access)
        resolve()
      }).catch(error => reject(error))
    })
  },
  registerGuest ({ dispatch }, { username, password }) {
    return new Promise((resolve, reject) => {
      app.api.registerGuest({ username, password }).then(data => {
        dispatch('useToken', data.access)
        resolve()
      }).catch(error => reject(error))
    })
  },
  useToken ({ commit, dispatch }, token) {
    try {
      const data = parseJwt(token)
      console.log(data)
      commit('setUser', {
        isGuest: data.is_guest,
        username: data.username,
        userId: data.user_id,
      })
      app.api.useToken(token)
    } catch (error) {
      dispatch('logout')
    }
  },
  logout ({ commit }) {
    app.api.logout()
    commit('unsetUser')
    router.push({ name: 'Login' })
  },
}

export default {
  namespaced: true,
  state,
  mutations,
  actions,
}
