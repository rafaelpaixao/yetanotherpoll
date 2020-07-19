<script>
import { Pie } from 'vue-chartjs'

const OPTIONS = {
  responsive: true,
  legend: {
    display: false,
  }
}

export default {
  extends: Pie,

  props: {
    dataset: {
      type: Object,
      required: true,
    },
    labels: {
      type: Array,
      required: true,
    },
  },

  mounted () {
    this.renderChart({ labels: this.labels, datasets: [this.dataset] }, OPTIONS)
  }
}
</script>
