<template>
  <a-simple-page>
    <template slot="title">Edit your poll</template>
    <PollForm :poll="poll" />
    <template slot="footer">
      <v-btn text color="accent" :to="{name: 'Polls'}">See all your polls</v-btn>
    </template>
  </a-simple-page>
</template>

<script>
import PollForm from '../components/PollForm'

export default {
  components: {
    PollForm
  },
  props: {
    poll: {
      type: Object,
      required: true
    }
  }
}
</script>
