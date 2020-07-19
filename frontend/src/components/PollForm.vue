<template>
  <app-loader v-if="loadingPoll" />

  <v-alert v-else-if="loadingError" type="error">{{error}}</v-alert>

  <v-form v-else v-model="formValid" @submit.prevent="submit">
    <v-textarea
      v-model="poll.title"
      :rules="$app.validation.poll.title"
      :counter="$app.constants.POLL_TITLE_MAX_LEN"
      autofocus
      auto-grow
      rows="1"
      placeholder="Type your question here"
      name="poll-title"
    ></v-textarea>

    <v-textarea
      v-model="poll.description"
      :rules="$app.validation.poll.description"
      :counter="$app.constants.POLL_DESC_MAX_LEN"
      auto-grow
      rows="1"
      placeholder="Brief explanation about the poll"
      name="poll-description"
    ></v-textarea>

    <div class="pb-5">
      <v-subheader class="px-0">OPTIONS</v-subheader>
      <v-text-field
        v-for="(option, i) in poll.options"
        :key="i"
        v-model="option.title"
        :rules="$app.validation.option.title"
        :counter="$app.constants.OPTION_TITLE_MAX_LEN"
        @click:append="removeOption(i)"
        append-icon="mdi-close"
        placeholder="Enter poll option"
        name="poll-option"
      ></v-text-field>
      <v-btn text color="success" class="mr-4" @click="addOption">Add Option</v-btn>
    </div>

    <div class="d-flex justify-end my-5">
      <v-btn v-if="editing" text :disabled="submiting" color="secondary" @click="cancel">Cancel</v-btn>
      <v-btn
        :loading="submiting"
        :disabled="submiting || !formValid"
        color="success"
        @click="submit"
      >{{ submitButtonText }}</v-btn>
    </div>
  </v-form>
</template>

<script>
export default {
  props: {
    pollId: {
      type: [String, Number],
      default: null
    }
  },

  data () {
    return {
      loadingPoll: true,
      loadingError: null,

      formValid: false,
      submiting: false,
      submitError: null,

      poll: {
        title: null,
        description: null,
        options: []
      }
    }
  },

  computed: {
    editing () {
      return !!this.poll.id
    },
    submitButtonText () {
      return this.editing ? 'Save changes' : 'Create new poll'
    },
  },

  mounted () {
    if (this.pollId) {
      this.loadPoll()
    } else {
      this.loadingPoll = false
      this.addOption()
    }
  },

  methods: {
    loadPoll () {
      this.$app.api.fetchPoll(this.pollId)
        .then(poll => (this.poll = poll))
        .catch(error => (this.error = error))
        .finally(() => (this.loadingPoll = false))
    },
    submit () {
      if (this.formValid) {
        this.submiting = true
        this.$app.api.submitPoll(this.poll)
          .then(poll => (this.$emit('success', poll)))
          .catch(error => (this.submitError = error))
          .finally(() => (this.submiting = false))
      }
    },
    addOption () {
      this.poll.options.push({ title: null })
    },
    removeOption (i) {
      this.poll.options.splice(i, 1)
    },
    cancel () {
      this.$emit('cancel')
    }
  }
}
</script>
