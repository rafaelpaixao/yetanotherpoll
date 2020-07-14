<template>
  <v-card class="mx-auto">
    <v-card-title>{{poll.title}}</v-card-title>

    <v-card-subtitle class="text-left">{{poll.description}}</v-card-subtitle>

    <v-card-text class="justify-center">
      <p
        v-for="(option, i) in poll.options"
        :key="i"
      >{{option.title}} - Votes: {{option.votesCount}}</p>TODO: chart
    </v-card-text>
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
}
</script>
