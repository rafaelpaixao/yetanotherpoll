<template>
  <app-loader v-if="loading" />

  <v-alert v-else-if="error" type="error">{{error}}</v-alert>

  <v-alert v-else-if="polls.length === 0" type="info">You don't have any polls!</v-alert>

  <div v-else>
    <v-list-item v-for="(poll, i) in polls" :key="i" :to="{name:'Vote', params:{ id: poll.id }}">
      <v-list-item-content>
        <v-list-item-title>{{poll.title}}</v-list-item-title>
      </v-list-item-content>
    </v-list-item>
  </div>
</template>

<script>
export default {
  data () {
    return {
      loading: true,
      error: null,
      polls: []
    }
  },

  mounted () {
    this.polls = this.$app.api.fetchUserPolls()
      .then(polls => (this.polls = polls))
      .catch(error => (this.error = error))
      .finally(() => (this.loading = false))
  }
}
</script>
