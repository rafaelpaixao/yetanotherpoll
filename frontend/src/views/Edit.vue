<template>
  <app-layout>
    <template slot="title">Edit your poll</template>

    <template v-slot:topright>
      <v-btn text color="accent" :to="{name: 'MyPolls'}">See all your polls</v-btn>
    </template>

    <PollForm :poll-id="id" @success="goToVote" @cancel="goToVote" @delete="goToMyPolls" />
  </app-layout>
</template>

<script>
import PollForm from '../components/PollForm'

export default {
  components: { PollForm },

  props: {
    id: {
      type: [String, Number],
      required: true,
    }
  },

  methods: {
    goToVote () {
      this.$router.push({ name: 'Vote', params: { id: this.id } })
    },
    goToMyPolls () {
      this.$router.push({ name: 'MyPolls' })
    }
  }
}
</script>
