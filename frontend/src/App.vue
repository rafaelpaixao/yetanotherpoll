<template>
  <v-app>
    <AppNavBar />
    <v-main>
      <app-header />
      <v-container fluid>
        <router-view />
      </v-container>
      <app-footer />
    </v-main>
  </v-app>
</template>

<script>
import AppNavBar from './components/AppNavBar'

export default {
  components: { AppNavBar }
}
</script>

<style lang="scss">
// Disable v-btn--active when using v-btn as router-link
// https://github.com/vuetifyjs/vuetify/issues/8172
.v-btn--router.v-btn--active {
  &::before,
  &.no-active::before {
    opacity: 0 !important;
  }
}
</style>
