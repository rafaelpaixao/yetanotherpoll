<template>
  <app-layout>
    <template slot="title">Login</template>

    <template v-slot:topright>
      <v-btn text color="accent" :to="{name: 'Register'}">Register</v-btn>
    </template>

    <LoginForm />
  </app-layout>
</template>

<script>
import LoginForm from '../components/LoginForm'

export default {
  components: { LoginForm },
}
</script>
