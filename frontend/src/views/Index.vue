<template>
  <app-layout>
    <template slot="title">Create your poll</template>

    <template v-slot:topright>
      <v-btn text color="accent" :to="{name: 'MyPolls'}">See all your polls</v-btn>
    </template>

    <PollForm @success="goToVote" />
  </app-layout>
</template>

<script>
import PollForm from '../components/PollForm'

export default {
  components: { PollForm },

  methods: {
    goToVote (poll) {
      this.$router.push({ name: 'Vote', params: { id: poll.id } })
    }
  }
}
</script>
