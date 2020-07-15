import Vue from 'vue'

Vue.component('app-layout', () =>
  import(/* webpackChunkName: "simplepage" */ './components/AppLayout.vue'))
