<template>
  <app-loader v-if="loadingPoll" />

  <v-alert v-else-if="loadError" type="error">Sorry, this poll is unavailable</v-alert>

  <v-card v-else class="mx-auto">
    <v-card-title>{{poll.title}}</v-card-title>

    <v-card-subtitle class="text-left">{{poll.description}}</v-card-subtitle>

    <v-card-text>
      <div>Total votes:{{totalVotes}}</div>
      <div class="d-flex justify-start mr-5 align-center" v-if="selectedOption">
        Your vote:
        <v-avatar :color="primaryColor" size="15" class="ml-2" />
      </div>
      <div class="d-flex justify-center">
        <PieChart
          :labels="chartLabels"
          :dataset="chartDataset"
          style="position:relative; width:50%"
        />
      </div>
      <div v-for="(option, i) in poll.options" :key="i" class="mb-3">
        <div>{{option.title}}</div>
        <v-progress-linear
          :title="option.count_votes"
          :color="option.color"
          height="20"
          :value="option.progress"
          dark
          striped
        >
          <strong>{{option.count_votes}}</strong>
        </v-progress-linear>
      </div>
    </v-card-text>

    <v-card-actions class="justify-end pb-5 px-5">
      <v-btn
        rounded
        color="primary"
        :to="{name:'Vote', params:{id:pollId}}"
        class="px-5"
      >Vote on this poll</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import PieChart from './PieChart'

export default {
  components: { PieChart },

  props: {
    pollId: {
      type: [String, Number],
      required: true,
    }
  },

  data () {
    return {
      loadingPoll: true,
      loadError: null,

      primaryColor: '#22CECE',
      secondaryColor: '#FFCD56',

      poll: null,
      selectedOption: null,
      totalVotes: 0,

      chartLabels: [],
      chartDataset: {
        label: 'Votes',
        data: [],
        backgroundColor: []
      },
    }
  },

  mounted () {
    this.$app.api.fetchPollWithResults(this.pollId)
      .then(data => {
        this.poll = data.poll
        if (data.vote) this.selectedOption = data.vote.option
        this.setColorsAndProgress()
        this.setChartLabelsAndDataset()
      })
      .catch(error => (this.loadError = error))
      .finally(() => (this.loadingPoll = false))
  },
  methods: {
    setColorsAndProgress () {
      this.totalVotes = this.poll.options.reduce((acc, option) => acc + option.count_votes, 0)
      this.poll.options.forEach(option => {
        option.progress = Math.floor(100 / this.totalVotes * option.count_votes)
        option.color = this.selectedOption === option.id ? this.primaryColor : this.secondaryColor
      })
    },
    setChartLabelsAndDataset () {
      this.poll.options.forEach(option => {
        this.chartLabels.push(option.title)
        this.chartDataset.data.push(option.count_votes)
        this.chartDataset.backgroundColor.push(option.color)
      })
    }
  }
}
</script>
