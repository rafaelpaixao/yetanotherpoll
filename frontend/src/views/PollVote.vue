<template>
  <a-page>
    <template v-slot:topright>
      <ShareButton :poll="poll" />
    </template>

    <template v-slot:default>
      <PollVoteForm :poll="poll" />
    </template>

    <template v-slot:topleft>
      <v-btn text color="accent" :to="{name: 'Polls'}">See all your polls</v-btn>
    </template>
  </a-page>
</template>

<script>
import PollVoteForm from '../components/PollVoteForm'
import ShareButton from '../components/ShareButton'

export default {
  components: {
    PollVoteForm,
    ShareButton
  },
  props: {
    poll: {
      type: Object,
      required: true
    }
  }
}
</script>
