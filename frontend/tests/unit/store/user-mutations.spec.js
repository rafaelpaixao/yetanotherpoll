import { mutations } from '../../../src/store/user'
import { app } from '../../../src/plugins/app'

// destructure assign `mutations`
const { setUsername, setToken } = mutations

const TEST_USERNAME = 'test_username'
const TEST_TOKEN = 'test_token'

describe('User Mutations', () => {
  it('Set username', () => {
    const state = { username: null }
    setUsername(state, TEST_USERNAME)
    expect(state.username).toMatch(TEST_USERNAME)
  })
  it('Set token', () => {
    const state = { username: null }
    setToken(state, TEST_TOKEN)
    expect(state.token).toMatch(TEST_TOKEN)
    // expect(localStorage(app.constants.LOCAL_STORAGE_TOKEN)).toMatch(TEST_TOKEN)
    expect(app.api.axios.defaults.headers.common.Authorization).toMatch('Bearer ' + TEST_TOKEN)
  })
})
