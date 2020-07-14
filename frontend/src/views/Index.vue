<template>
  <a-simple-page>
    <template slot="title">Create your poll</template>
    <PollForm />
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
  }
}
</script>
