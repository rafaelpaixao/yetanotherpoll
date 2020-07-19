import { POLL_TITLE_MAX_LEN, POLL_DESC_MAX_LEN, OPTION_TITLE_MAX_LEN } from './constants'

export default {
  username: [
    (v) => !!v || 'Username is required',
  ],
  password: [
    (v) => !!v || 'Password is required',
  ],
  poll: {
    title: [
      (v) => !!v || 'Title is required',
      (v) =>
        !!v && v.length > POLL_TITLE_MAX_LEN
          ? `Title must be less than ${POLL_TITLE_MAX_LEN} characters` : true,
    ],
    description: [
      (v) => !!v || 'Description is required',
      (v) => !!v && v.length > POLL_DESC_MAX_LEN ? `Description must be less than ${POLL_DESC_MAX_LEN} characters` : true
    ],

  },
  option: {
    title: [
      (v) => !!v || 'Option is required',
      (v) =>
        !!v && v.length > POLL_TITLE_MAX_LEN
          ? `Option must be less than ${OPTION_TITLE_MAX_LEN} characters` : true,
    ],
  }
}
