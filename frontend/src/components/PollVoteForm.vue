<template>
  <v-card class="mx-auto">
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

    <v-alert v-if="!sending && error" type="error">{{error}}</v-alert>

    <v-card-actions class="justify-space-between pb-5 px-5">
      <v-btn text color="accent" :to="{name:'PollEdit'}" class="px-5">Edit this poll</v-btn>
      <v-btn
        x-large
        rounded
        :loading="sending"
        :disabled="sending || !selectedOption"
        color="success"
        @click="submit"
        class="px-5"
      >Vote</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: {
    poll: {
      type: Object,
      required: true
    }
  },
  data () {
    return {
      error: null,
      isValid: false,
      sending: false,
      selectedOption: null,
    }
  },
  methods: {
    async submit () {
      this.sending = true
      this.error = null
      try {
        await this.$app.api.voteOnPoll(this.selectedOption)
        this.$router.push({
          name: 'PollResult',
          params: this.$router.params,
        })
      } catch (error) {
        this.error = error
      } finally {
        this.sending = false
      }
    }
  }
}
</script>
