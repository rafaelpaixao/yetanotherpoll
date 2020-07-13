<template>
  <v-app>
    <v-app-bar app color="transparent" flat short>
      <v-spacer />
      <v-btn to="Index">Create a Poll</v-btn>
      <v-btn text to="Login">Login</v-btn>
      <v-btn text to="Register">Register</v-btn>
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
