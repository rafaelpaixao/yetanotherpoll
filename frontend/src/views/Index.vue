<template>
  <app-layout>
    <template slot="title">Create your poll</template>

    <template v-slot:topright>
      <v-btn text color="accent" :to="{name: 'MyPolls'}">See all your polls</v-btn>
    </template>

    <PollForm />
  </app-layout>
</template>

<script>
import PollForm from '../components/PollForm'

export default {
  components: { PollForm },
}
</script>
