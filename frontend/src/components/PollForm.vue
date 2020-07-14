<template>
  <v-card class="mx-auto">
    <v-card-text>
      <v-form v-model="isValid" @submit="submit">fields...</v-form>
    </v-card-text>
    <v-card-actions class="justify-end">
      <v-btn
        x-large
        rounded
        :loading="sending"
        :disabled="sending || !isValid"
        color="success"
        @click="submit"
        class="mb-5 mr-5 px-5"
      >Create Poll</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  data () {
    return {
      isValid: false,
      sending: false,
    }
  },
  methods: {
    submit () {
      console.log('submit')
    }
  }
}
</script>
