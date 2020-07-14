<template>
  <div class="text-center">
    <div v-if="loadingPoll">
      <v-progress-circular indeterminate color="primary" />
    </div>
    <v-alert v-else-if="error">{{error}}</v-alert>
    <router-view v-else-if="poll" :poll="poll" />
  </div>
</template>

<script>
export default {
  props: {
    pollCode: {
      type: [String, Number],
      default: null
    }
  },
  data () {
    return {
      loadingPoll: true,
      error: null,
      polls: null
    }
  },
  async mounted () {
    try {
      this.poll = await this.$app.api.fetchOnePoll(this.pollCode)
    } catch (error) {
      this.error = error
    } finally {
      this.loadingPoll = false
    }
  }
}
</script>
