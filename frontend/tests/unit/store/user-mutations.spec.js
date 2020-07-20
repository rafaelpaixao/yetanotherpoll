import { mutations, state } from '../../../src/store/user'

// destructure assign `mutations`
const { setUser, unsetUser } = mutations

const TEST_USERNAME = 'test_username'
const TEST_USER_ID = 'test_user_id'
const TEST_USER_IS_GUEST = true

describe('User Mutations', () => {
  it('Set user', () => {
    setUser(state, { username: TEST_USERNAME, userId: TEST_USER_ID, isGuest: TEST_USER_IS_GUEST })
    expect(state.username).toMatch(TEST_USERNAME)
    expect(state.userId).toMatch(TEST_USER_ID)
    expect(state.isGuest).toBeTruthy()
  })
  it('Unset user', () => {
    unsetUser(state)
    expect(state.username).toBeNull()
    expect(state.userId).toBeNull()
    expect(state.isGuest).toBeFalsy()
  })
})
