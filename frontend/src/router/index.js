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
    props: true,
    component: () =>
      import(/* webpackChunkName: "poll" */ '../views/Poll.vue'),
    children: [
      {
        path: '',
        name: 'PollVote',
        props: true,
        component: () =>
          import(/* webpackChunkName: "pollvote" */ '../views/PollVote.vue'),
      },
      {
        path: 'edit',
        name: 'PollEdit',
        props: true,
        component: () =>
          import(/* webpackChunkName: "polledit" */ '../views/PollEdit.vue'),
      },
      {
        path: 'result',
        name: 'PollResult',
        props: true,
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
