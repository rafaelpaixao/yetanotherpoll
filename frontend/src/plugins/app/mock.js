import { Poll, Option, Vote } from './models'

// CONSTS
const loremIpsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore'
const MAX_N_VOTES = 20
const MAX_N_OPTIONS = 5
const MAX_N_POLLS = 10

// Simulates a request that fails
const fail = (error, seconds = 2) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      reject(error)
    }, seconds * 1000)
  })
}

// Simulates a successuful request
const success = (data, seconds = 2) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(data)
    }, seconds * 1000)
  })
}

class MockData {
  constructor () {
    // Holds the next id to be used when mocking that entity
    this.NEXT_POLL_ID = 1
    this.NEXT_OPTION_ID = 1
    this.NEXT_ANDSWER_ID = 1
    // The actual mocked data
    this.polls = []
    this.options = []
    this.votes = []
  }

  // Increments the ids
  getPollId () { return this.NEXT_POLL_ID++ }
  getOptionId () { return this.NEXT_OPTION_ID++ }
  getVoteId () { return this.NEXT_ANDSWER_ID++ }

  // Creates a mocked poll from user data
  createPoll (title, description, options) {
    const id = this.getPollId()
    const poll = new Poll({
      id,
      title: title,
      description: description
    })
    options.forEach(option => {
      poll.options.push(new Option({
        id: this.getOptionId(),
        title: option.title,
        poll: poll
      }))
    })
    this.polls.push(poll)
    this.options.concat(poll.options)
    return success(poll)
  }

  findPoll (id) {
    const result = this.polls.filter(p => '' + p.id === '' + id)
    return result.length === 0 ? fail('Poll not found') : success(result[0])
  }

  // Edits a mocked poll with user data
  editPoll (id, title, description, options) {
    const poll = this.polls.filter(p => p.id === id)[0]
    poll.title = title
    poll.description = description
    return success(poll)
  }

  voteOnPoll (optionId) {
    const result = this.options.filter(o => o.id === optionId)

    if (result.length === 0) return fail('Option not found')

    const option = result[0]
    const vote = this.votes.push(new Vote({
      id: this.getVoteId(),
      option: option.id,
    }))
    this.votes.push(vote)
    option.votesCount++
    return success(vote)
  }
}

export const Mock = new MockData()

const genVotes = option => {
  const n = Math.floor(Math.random() * MAX_N_VOTES) + 1
  let i = n
  while (i > 0) {
    const id = Mock.getVoteId()
    Mock.votes.push(new Vote(id, option))
    i--
  }
  return n
}

const genOptions = poll => {
  let n = Math.floor(Math.random() * MAX_N_OPTIONS) + 1
  while (n > 0) {
    const id = Mock.getOptionId()
    const option = new Option({ id, title: 'Option ' + id, poll: poll.id })
    option.votesCount = genVotes(option.id)
    poll.options.push(option)
    Mock.options.push(option)
    n--
  }
}

const genPolls = () => {
  let n = Math.floor(Math.random() * MAX_N_POLLS) + 1
  while (n > 0) {
    const id = Mock.getPollId()
    const poll = new Poll({ id, title: 'Test Poll ' + id, description: loremIpsum })
    genOptions(poll)
    Mock.polls.push(poll)
    n--
  }
}

class MockApi {
  constructor () {
    genPolls()
    console.log(Mock)
  }

  fetchAllPolls () {
    return success(Mock.polls)
  }

  fetchOnePoll (id) {
    return Mock.findPoll(id)
  }

  createPoll (data) {
    return Mock.createPoll(data.title, data.description, data.options)
  }

  editPoll (data) {
    return Mock.editPoll(data.id, data.title, data.description, data.options)
  }

  voteOnPoll (optionId) {
    return Mock.voteOnPoll(optionId)
  }
}

export default new MockApi()
