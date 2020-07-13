<template>
  <div>/poll/{{pollCode}}/edit</div>
</template>

<script>

export default {
  components: {
  },
  props: {
    pollCode: {
      type: String,
      required: true
    }
  }
}
</script>
