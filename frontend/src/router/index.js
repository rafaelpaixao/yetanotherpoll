import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Index',
    component: () =>
      import(/* webpackChunkName: "index" */ '../views/Index.vue'),
  },
  {
    path: '/login',
    name: 'Login',
    component: () =>
      import(/* webpackChunkName: "login" */ '../views/Login.vue'),
  },
  {
    path: '/register',
    name: 'Register',
    component: () =>
      import(/* webpackChunkName: "register" */ '../views/Register.vue'),
  },
  {
    path: '/my-polls',
    name: 'MyPolls',
    component: () =>
      import(/* webpackChunkName: "index" */ '../views/MyPolls.vue'),
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
