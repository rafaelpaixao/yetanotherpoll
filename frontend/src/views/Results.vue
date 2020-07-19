<template>
  <app-layout>
    <template v-slot:title>Poll Results</template>

    <ResultChart :poll-id="id" />
  </app-layout>
</template>

<script>
import ResultChart from '../components/ResultChart'

export default {
  components: { ResultChart },

  props: {
    id: {
      type: [String, Number],
      required: true,
    }
  },
}
</script>
