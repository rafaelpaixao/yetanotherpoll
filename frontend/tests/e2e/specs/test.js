// https://docs.cypress.io/api/introduction/api.html

describe('Test router', () => {
  it('Visits Index', () => {
    cy.visit('/')
    cy.contains('h6', 'Create your poll')
  })

  it('Visits Login', () => {
    cy.visit('/login')
    cy.contains('h6', 'Login')
  })

  it('Visits Register', () => {
    cy.visit('/register')
    cy.contains('h6', 'Register')
  })

  it('Visits My Polls', () => {
    cy.visit('/my-polls')
    cy.contains('h6', 'Your polls')
  })
})
