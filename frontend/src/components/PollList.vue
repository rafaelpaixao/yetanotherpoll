<template>
  <v-card class="mx-auto">
    <v-card-text>
      <v-alert
        v-if="polls.length === 0"
        type="info"
      >You don't have any polls, click on the button bellow to create a new poll!</v-alert>
      <div v-else>
        <v-list-item
          v-for="(poll, i) in polls"
          :key="i"
          :to="{name:'PollVote', params:{ pollCode: poll.id }}"
        >
          <v-list-item-content>
            <v-list-item-title>{{poll.title}}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: {
    polls: {
      type: Array,
      default: () => []
    }
  }
}
</script>
