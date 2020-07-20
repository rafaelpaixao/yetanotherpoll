/*
  Vue.js plugin dedicated to the business logic.

  The instance is a singleton and can be imported as
    import { app } from '../app'

  Also it's available in the Vue instance like:
    this.$app.api....
*/

import api from './api'
import constants from './constants'
import validation from './validation'
import { tokenStorage } from './storage'

export const app = {
  api,
  constants,
  validation,
}

export default {
  install: (Vue, options) => {
    app.api.setBaseUrl(process.env.VUE_APP_API_URL)
    Vue.prototype.$app = app

    app.api.addResponseInterceptors({
      success: response => {
        // Use access token, if response has one
        if (response.headers.token) {
          options.store.dispatch('user/useToken', response.headers.token)
        }
        // Return data directly
        return response.data
      },
      error: error => {
        // Logout user if response has unauthorized status
        if (error.response.status === 401) options.store.dispatch('user/logout')
        Promise.reject(error)
      }
    })

    // Use token from local storage
    if (tokenStorage.exists()) options.store.dispatch('user/useToken', tokenStorage.get())
  },
}
