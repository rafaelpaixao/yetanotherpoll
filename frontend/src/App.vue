<template>
  <v-app>
    <v-app-bar app color="transparent" flat short>
      <v-spacer />
      <v-btn :to="{name: 'Index'}" active-class="no-active" color="accent" outlined>Create a Poll</v-btn>
      <v-btn :to="{name: 'Login'}" active-class="no-active" small text class="mx-5">Login</v-btn>
      <v-btn :to="{name: 'Register'}" active-class="no-active" small text>Register</v-btn>
    </v-app-bar>
    <v-main>
      <app-header />
      <v-container fluid>
        <router-view />
      </v-container>
      <app-footer />
    </v-main>
  </v-app>
</template>

<style lang="scss" scoped>
// Disable v-btn--active when using v-btn as router-link
// https://github.com/vuetifyjs/vuetify/issues/8172
.v-btn--active.no-active::before {
  opacity: 0 !important;
}
</style>
