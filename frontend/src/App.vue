<template>
  <v-app>
    <v-main>
      <AHeader />
      <router-view />
    </v-main>
    <AFooter />
  </v-app>
</template>

<script>
import AFooter from './components/AFooter'
import AHeader from './components/AHeader'

export default {
  components: { AFooter, AHeader }
}
</script>
