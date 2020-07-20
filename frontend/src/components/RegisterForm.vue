<script>
import BaseAuthForm from './BaseAuthForm'
import { mapState } from 'vuex'

export default {
  extends: BaseAuthForm,
  data () {
    return {
      buttonText: 'Register',
    }
  },

  computed: {
    dispatchTo () {
      return this.isGuest ? 'registerGuest' : 'register'
    },
    ...mapState('user', ['isGuest']),
  }
}
</script>
