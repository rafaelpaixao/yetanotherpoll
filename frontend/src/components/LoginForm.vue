<script>
import BaseAuthForm from './BaseAuthForm'

export default {
  extends: BaseAuthForm,
  data () {
    return {
      buttonText: 'Login',
      dispatchTo: 'login',
    }
  }
}
</script>
