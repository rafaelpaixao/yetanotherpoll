<template>
  <a-page>
    <template v-slot:title>Your polls</template>

    <template v-slot:topright>
      <v-btn text color="accent" :to="{name:'PollCreate'}" class="px-5">Create a poll</v-btn>
    </template>

    <template v-slot:default>
      <div class="text-center" v-if="loadingPolls">
        <v-progress-circular indeterminate color="primary" />
      </div>
      <v-alert v-else-if="error" />
      <PollList v-else-if="polls" :polls="polls" />
    </template>
  </a-page>
</template>

<script>
import PollList from '../components/PollList'

export default {
  components: {
    PollList
  },
  data () {
    return {
      loadingPolls: true,
      error: null,
      polls: null
    }
  },
  async mounted () {
    try {
      this.polls = await this.$app.api.fetchAllPolls()
    } catch (error) {
      this.error = error
    } finally {
      this.loadingPolls = false
    }
  }
}
</script>
