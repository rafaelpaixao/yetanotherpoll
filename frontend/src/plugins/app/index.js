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

export const app = {
  api,
  constants,
  validation,
}

export default {
  install: (Vue, options) => {
    app.api.setBaseUrl(process.env.VUE_APP_API_URL)
    Vue.prototype.$app = app
  },
}
