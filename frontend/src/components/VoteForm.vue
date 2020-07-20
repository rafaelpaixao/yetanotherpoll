<template>
  <app-loader v-if="loadingPoll" />

  <v-alert v-else-if="loadError" type="error">Sorry, this poll is unavailable</v-alert>

  <v-card v-else class="mx-auto">
    <v-card-title>{{poll.title}}</v-card-title>

    <v-card-subtitle class="text-left">{{poll.description}}</v-card-subtitle>

    <v-card-text class="justify-center px-5">
      <v-radio-group v-model="selectedOption" class="px-5">
        <v-radio
          v-for="(option, i) in poll.options"
          :key="i"
          :label="option.title"
          :value="option.id"
          class="my-3"
        ></v-radio>
      </v-radio-group>
    </v-card-text>

    <v-alert v-if="!voting && voteError" type="error">{{voteError}}</v-alert>

    <v-card-actions class="pb-5 px-5" :class="isOwner ? 'justify-space-between': 'justify-end'">
      <v-btn v-if="isOwner" x-large text @click="$emit('edit')" color="accent" class="px-5">Edit</v-btn>
      <v-btn
        x-large
        rounded
        :loading="voting"
        :disabled="voting || !selectedOption"
        color="success"
        @click="vote"
        class="px-5"
      >Vote</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { mapState } from 'vuex'

export default {
  props: {
    pollId: {
      type: [String, Number],
      required: true,
    }
  },

  data () {
    return {
      loadingPoll: true,
      loadError: null,

      voting: false,
      voteError: null,

      poll: null,
      selectedOption: null,
    }
  },

  computed: {
    isOwner () {
      return this.userId === this.poll.author
    },
    ...mapState('user', ['userId'])
  },

  mounted () {
    this.$app.api.fetchPoll(this.pollId)
      .then(data => {
        this.poll = data.poll
        if (data.vote) this.selectedOption = data.vote.option
      })
      .catch(error => (this.loadError = error))
      .finally(() => (this.loadingPoll = false))
  },

  methods: {
    vote () {
      this.voting = true
      this.$app.api.submitVote(this.selectedOption)
        .then(() => (this.$emit('success')))
        .catch(error => (this.voteError = error))
        .finally(() => (this.voting = false))
    },
  }
}
</script>
