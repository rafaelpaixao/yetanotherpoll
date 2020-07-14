export class Poll {
  constructor ({ id = null, title = null, description = null, options = [] }) {
    this.id = id
    this.title = title
    this.description = description
    this.options = options
  }
}

export class Option {
  constructor ({ id = null, title = null, poll = null, votesCount = null }) {
    this.id = id
    this.title = title
    this.votesCount = votesCount
    this.poll = poll
  }
}

export class Vote {
  constructor ({ id = null, option = null }) {
    this.id = id
    this.option = option
  }
}
