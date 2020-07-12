<template>
  <v-app>
    <v-main>
      <router-view />
    </v-main>
    <a-footer />
  </v-app>
</template>

<script>
import AFooter from './components/AFooter'

export default {
  components: { AFooter }
}
</script>
