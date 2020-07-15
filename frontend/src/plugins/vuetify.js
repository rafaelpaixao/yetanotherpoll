import Vue from 'vue'
import Vuetify from 'vuetify/lib'

Vue.use(Vuetify)

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: '#04B03E',
        secondary: '#607D8B',
        accent: '#74543D',
        error: '#D81B60',
        info: '#3F51B5',
        warning: '#E57373'
      },
    },
  },
})
