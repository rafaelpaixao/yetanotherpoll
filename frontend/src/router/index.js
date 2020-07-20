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
  {
    path: '/poll/:id',
    name: 'Vote',
    props: true,
    component: () =>
      import(/* webpackChunkName: "vote" */ '../views/Vote.vue'),
  },
  {
    path: '/poll/:id/edit',
    name: 'Edit',
    props: true,
    component: () =>
      import(/* webpackChunkName: "edit" */ '../views/Edit.vue'),
  },
  {
    path: '/poll/:id/results',
    name: 'Results',
    props: true,
    component: () =>
      import(/* webpackChunkName: "results" */ '../views/Results.vue'),
  },

  {
    path: '*',
    component: () =>
      import(/* webpackChunkName: "pagenotfound" */ '../views/PageNotFound.vue'),
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
