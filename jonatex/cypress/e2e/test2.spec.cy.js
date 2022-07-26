describe('google test2', () => {
  it('buscar en google linux distro y hacer click en el primer resultado', () => {
   cy.visit('https://www.google.com/')
   cy.get('[name="q"]').type('linux distro');
    cy.get('[name="q"]').type('{enter}');
    cy.get( "#search .g a").first().click();
  })
})