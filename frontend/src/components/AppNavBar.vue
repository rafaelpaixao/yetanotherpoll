<template>
  <v-app-bar app color="transparent" flat short>
    <v-spacer />
    <v-btn :to="{name: 'Index'}" active-class="no-active" color="accent" outlined>Create a Poll</v-btn>

    <template v-if="username">
      <v-menu offset-y>
        <template v-slot:activator="{ on, attrs }">
          <v-btn color="transparent" rounded depressed class="ml-5 pr-0" v-bind="attrs" v-on="on">
            {{username.split('@')[0]}}
            <v-avatar right>
              <v-icon>mdi-account-circle</v-icon>
            </v-avatar>
          </v-btn>
        </template>
        <v-list>
          <v-list-item @click="logout">
            <v-list-item-title>Logout</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </template>

    <template v-else>
      <v-btn :to="{name: 'Login'}" active-class="no-active" small text class="mx-5">Login</v-btn>
      <v-btn :to="{name: 'Register'}" active-class="no-active" small text>Register</v-btn>
    </template>
  </v-app-bar>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  computed: {
    ...mapState('user', ['username'])
  },

  methods: {
    ...mapActions('user', ['logout'])
  }
}
</script>
