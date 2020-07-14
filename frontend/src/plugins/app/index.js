import mockApi from './mock'

export const app = {}

export default {
  install: (Vue, options) => {
    app.api = mockApi
    Vue.prototype.$app = app
  },
}
