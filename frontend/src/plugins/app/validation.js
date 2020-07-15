export default {
  username: [
    (v) => !!v || 'Username is required',
  ],
  password: [
    (v) => !!v || 'Password is required',
  ],
}
