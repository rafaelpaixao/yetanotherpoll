<template>
  <a-simple-page>
    <template slot="title">Register</template>
    <RegisterForm />
    <template slot="footer">
      Already have an account?
      <router-link :to="{name: 'Login'}">Login now!</router-link>
    </template>
  </a-simple-page>
</template>

<script>
import RegisterForm from '../components/RegisterForm'

export default {
  components: {
    RegisterForm
  }
}
</script>
