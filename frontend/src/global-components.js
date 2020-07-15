import Vue from 'vue'

Vue.component('app-layout', () =>
  import(/* webpackChunkName: "simplepage" */ './components/AppLayout.vue'))

Vue.component('app-header', () =>
  import(/* webpackChunkName: "simplepage" */ './components/AppHeader.vue'))

Vue.component('app-footer', () =>
  import(/* webpackChunkName: "simplepage" */ './components/AppFooter.vue'))
