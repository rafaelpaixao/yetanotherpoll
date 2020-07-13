<template>
  <v-app>
    <v-app-bar app color="transparent" flat short>
      <v-spacer />
      <v-btn
        :to="{name: 'PollCreate'}"
        active-class="no-active"
        color="accent"
        outlined
      >Create a Poll</v-btn>
      <v-btn text class="mx-5" :to="{name: 'Login'}" active-class="no-active" small>Login</v-btn>
      <v-btn text :to="{name: 'Register'}" active-class="no-active" small>Register</v-btn>
    </v-app-bar>
    <v-main>
      <AHeader />
      <v-container fluid>
        <router-view />
      </v-container>
      <AFooter />
    </v-main>
  </v-app>
</template>

<script>
import AFooter from './components/AFooter'
import AHeader from './components/AHeader'

export default {
  components: { AFooter, AHeader }
}
</script>
<style lang="scss" scoped>
// Disable v-btn--active when using v-btn as router-link
// https://github.com/vuetifyjs/vuetify/issues/8172
.v-btn--active.no-active::before {
  opacity: 0 !important;
}
</style>
