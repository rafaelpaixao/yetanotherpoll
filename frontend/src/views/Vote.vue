<template>
  <app-layout>
    <template v-slot:topleft>
      <v-btn text color="accent" :to="{name: 'MyPolls'}">My Polls</v-btn>
    </template>
    <template v-slot:topright>
      <ShareButton :poll-id="id"/>
    </template>
    <VoteForm :poll-id="id" @success="goToResults" @edit="goToEdit" />
  </app-layout>
</template>

<script>
import VoteForm from '../components/VoteForm'
import ShareButton from '../components/ShareButton'

export default {
  components: { ShareButton, VoteForm },

  props: {
    id: {
      type: [String, Number],
      required: true,
    }
  },

  methods: {
    goToResults () {
      this.$router.push({ name: 'Results', params: { id: this.id } })
    },
    goToEdit () {
      this.$router.push({ name: 'Edit', params: { id: this.id } })
    }
  }
}
</script>
