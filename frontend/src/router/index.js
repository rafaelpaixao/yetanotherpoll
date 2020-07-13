import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'PollCreate',
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
    path: '/polls',
    name: 'Polls',
    component: () =>
      import(/* webpackChunkName: "polls" */ '../views/Polls.vue'),
  },
  {
    path: '/poll/:pollCode',
    name: 'Poll',
    props: true,
    component: () =>
      import(/* webpackChunkName: "poll" */ '../views/Poll.vue'),
    children: [
      {
        path: 'edit',
        name: 'PollEdit',
        component: () =>
          import(/* webpackChunkName: "polledit" */ '../views/PollEdit.vue'),
      },
      {
        path: 'result',
        name: 'PollResult',
        component: () =>
          import(/* webpackChunkName: "pollresult" */ '../views/PollResult.vue'),
      }
    ]
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

export default router
