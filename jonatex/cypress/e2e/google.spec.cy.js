describe('google test', () => {
  it('searches carros deportivos and opens second result', () => {
    cy.visit('https://www.google.com/');
    cy.get('[name="q"]').type('carros deportivos');
    cy.get('[name="q"]').type('{enter}');
    cy.get('[class^="g"][lang="es"] a').eq(3).click();
  })
})