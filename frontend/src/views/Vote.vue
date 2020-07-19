<template>
  <app-layout>
    <template v-slot:title>Vote on poll</template>

    <VoteForm :poll-id="id" @success="goToResults" @edit="goToEdit" />
  </app-layout>
</template>

<script>
import VoteForm from '../components/VoteForm'

export default {
  components: { VoteForm },

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
