

describe('aaaa', () => {
        
    
    it('bbb', () => {
        cy.visit('https://linkedin.com');
        
        cy.get('.nav__button-secondary').click();
        cy.get('#username').type('mihai_ratiu@yahoo.com');
        cy.get('#password').type('.....');
        cy.get('.btn__primary--large').click();



    })

})