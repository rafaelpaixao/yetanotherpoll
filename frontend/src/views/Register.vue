<template>
  <app-layout>
    <template slot="title">Register</template>

    <template v-slot:topright>
      <v-btn text color="accent" :to="{name: 'Login'}">Login</v-btn>
    </template>

    <RegisterForm @success="goToMyPolls" />
  </app-layout>
</template>

<script>
import RegisterForm from '../components/RegisterForm'

export default {
  components: { RegisterForm },

  methods: {
    goToMyPolls () {
      this.$router.push({ name: 'MyPolls' })
    }
  }
}
</script>
