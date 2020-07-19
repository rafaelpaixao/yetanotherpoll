import Vue from 'vue'

Vue.component('app-layout', () =>
  import(/* webpackChunkName: "simplepage" */ './components/AppLayout.vue'))

Vue.component('app-loader', () =>
  import(/* webpackChunkName: "simplepage" */ './components/AppLoader.vue'))
