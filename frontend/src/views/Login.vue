<template>
  <a-simple-page>
    <template slot="title">Login</template>
    <LoginForm />
    <template slot="footer">
      Doesn't have an account?
      <router-link :to="{name: 'Register'}">Register now!</router-link>
    </template>
  </a-simple-page>
</template>

<script>
import LoginForm from '../components/LoginForm'

export default {
  components: {
    LoginForm
  }
}
</script>
