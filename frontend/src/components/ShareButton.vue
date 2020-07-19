<template>
  <v-dialog v-model="dialog" max-width="300">
    <template v-slot:activator>
      <v-btn small color="warning" @click="share">Share</v-btn>
    </template>

    <v-card>
      <v-toolbar dense>
        <v-toolbar-title>Share this poll</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon>
          <v-icon @click="dialog = false">mdi-close</v-icon>
        </v-btn>
      </v-toolbar>
      <v-card-text class="vue-social-sharing pt-5 text-center">
        <v-text-field id="fullUrl" v-model="fullUrl" label="Poll link" type="text" />

        <v-transition-fade>
          <v-btn v-if="!copied" color="primary" @click="copyLinkToClipboard">Copy link</v-btn>
          <v-btn v-else color="primary" text>Copied!</v-btn>
        </v-transition-fade>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  props: {
    pollId: {
      type: [String, Number],
      required: true,
    }
  },

  computed: {
    fullUrl () {
      return this.$app.constants.APP_BASE_URL + this.$router.resolve({ name: 'Vote', params: { id: this.pollId } }).href
    },
  },

  data () {
    return {
      dialog: false,
      copied: false,
    }
  },

  methods: {
    share () {
      // Native share requires HTTPS
      // https://developer.mozilla.org/en-US/docs/Web/API/Navigator/share
      if (navigator && navigator.share) {
        navigator.share({
          title: 'Poll for you',
          text: 'Check this poll I made using YetAnotherPoll',
          url: this.fullUrl,
        })
      } else {
        // Fallback to menu with link
        this.dialog = true
      }
    },
    copyLinkToClipboard () {
      const $el = document.querySelector('#fullUrl')
      $el.select()
      // $el.setSelectionRange(0, 99999) /* For mobile devices */
      /* Copy the text inside the text field */
      document.execCommand('copy')
      this.copied = true
    },
  },

  watch: {
    dialog (newVal) {
      if (newVal) this.copied = false
    }
  }
}
</script>
