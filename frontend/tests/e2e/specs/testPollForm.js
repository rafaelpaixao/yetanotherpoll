// https://docs.cypress.io/api/introduction/api.html

describe('Test poll form', () => {
  it('Visits Index', () => {
    cy.visit('/')
    cy.contains('h6', 'Create your poll')

    cy.get('#inputPollTitle').type('Do you like polls?')
    cy.get('#inputPollDescription').type('Just a test')
    cy.get('#inputPollOption0').type('Yes')
    cy.get('#btnAddOption').click()
    cy.get('#inputPollOption1').type('Of course')
    cy.get('form').submit()
  })
})
