describe('empty spec', () => {
  it('Boton pokedex se le puede hacer click', () => {
    cy.visit('https://www.pokemon.com/us/')
    cy.get('[href="/us/pokedex/"]').first().click()
  })
})