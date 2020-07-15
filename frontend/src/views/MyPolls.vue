<template>
  <app-layout>
    <template v-slot:title>Your polls</template>

    <template v-slot:topright>
      <v-btn text color="accent" :to="{name:'Index'}" class="px-5">Create a poll</v-btn>
    </template>

    <PollList />
  </app-layout>
</template>

<script>
import PollList from '../components/PollList'

export default {
  components: { PollList },
}
</script>
