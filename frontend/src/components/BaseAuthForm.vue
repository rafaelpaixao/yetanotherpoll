<template>
  <v-card class="mx-auto">
    <v-card-text>
      <v-form v-model="formValid" @submit.prevent="submit">
        <v-text-field
          v-model="username"
          :rules="$app.validation.username"
          autofocus
          name="username"
          label="Username"
        />
        <v-text-field
          v-model="password"
          :rules="$app.validation.password"
          name="password"
          type="password"
          label="Password"
        />
      </v-form>

      <v-scale-transition>
        <v-alert v-if="error" type="error" class="mb-5 mx-3">{{error}}</v-alert>
      </v-scale-transition>
    </v-card-text>

    <v-card-actions class="justify-end">
      <v-btn
        x-large
        rounded
        :loading="sending"
        :disabled="sending || !formValid"
        color="success"
        @click="submit"
        class="mb-5 mr-5 px-5"
      >{{buttonText}}</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  data () {
    return {
      error: null,
      sending: false,

      formValid: false,
      username: '',
      password: '',

      // Must be setted
      // buttonText: 'buttonText',
      // dispatchTo: 'dispatchTo'
    }
  },
  methods: {
    submit () {
      if (this.formValid) {
        const data = {
          username: this.username,
          password: this.password,
        }
        this.submiting = true
        this.$store.dispatch('user/' + this.dispatchTo, data)
          .then(() => (this.$emit('success')))
          .catch(error => {
            const data = error.response.data
            this.error = data.detail || data.username[0] || data.password[0]
          })
          .finally(() => (this.submiting = false))
      }
    },
  },
}
</script>
