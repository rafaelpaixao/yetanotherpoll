<template>
  <div>
    <div>/poll/{{pollCode}}</div>
    <router-view :poll-code="pollCode" />
  </div>
</template>

<script>

export default {
  components: {
  },
  props: {
    pollCode: {
      type: String,
      default: null
    }
  },
}
</script>
