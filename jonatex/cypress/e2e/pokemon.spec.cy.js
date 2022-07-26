describe('pokemon test', () => {
  it('Navigate to the Pokedex and Search by Name </br>', () => {
    cy.visit('https://www.pokemon.com/us/');
    cy.get("#onetrust-accept-btn-handler", {timeout:30000}).should("be.visible").click();
    cy.get('.explore > a').click();
    cy.get('[href="/us/pokedex/"]').click();
    cy.get("#searchInput").type("Pikachu");
    cy.get(".filter-text-search > #search").click();
    cy.get("#search.button.button-search").click()
  })
})