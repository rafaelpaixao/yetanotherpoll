import { LOCAL_STORAGE_TOKEN_KEY } from './constants'

class Storage {
  constructor (key) {
    this.key = key
  }

  exists () {
    return !!localStorage.getItem(this.key)
  }

  get () {
    return localStorage.getItem(this.key)
  }

  set (value) {
    return localStorage.setItem(this.key, value)
  }

  delete () {
    localStorage.removeItem(this.key)
  }
}

export const tokenStorage = new Storage(LOCAL_STORAGE_TOKEN_KEY)
