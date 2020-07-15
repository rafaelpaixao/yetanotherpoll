<template>
  <v-card class="mx-auto">
    <v-card-text>
      <v-form v-model="isValid" @submit="submit">
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
    </v-card-text>
    <v-scale-transition>
      <v-alert v-if="error" type="error" class="mb-5 mx-3">{{error}}</v-alert>
    </v-scale-transition>
    <v-card-actions class="justify-end">
      <v-btn
        x-large
        rounded
        :loading="sending"
        :disabled="sending || !isValid"
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
      isValid: false,
      sending: false,
      username: '',
      password: '',
      buttonText: 'buttonText',
      dispatchTo: 'dispatchTo'
    }
  },
  methods: {
    async submit () {
      try {
        await this.$store.dispatch('user/' + this.dispatchTo, {
          username: this.username,
          password: this.password,
        })
        this.$router.push({ name: 'Index' })
      } catch (error) {
        const data = error.response.data
        this.error = data.detail || data.username[0] || data.password[0]
      } finally {
        this.sending = false
      }
    },
  },
}
</script>
