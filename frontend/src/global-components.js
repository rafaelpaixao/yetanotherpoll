import Vue from 'vue'

Vue.component('a-simple-page', () =>
  import(/* webpackChunkName: "simplepage" */ './components/ASimplePage.vue'))

Vue.component('a-page', () =>
  import(/* webpackChunkName: "simplepage" */ './components/AppPage.vue'))
