describe('site google.com',() => {
//test nr 1 

    it('cautare basic' , () => {   
     cy.visit('https://google.com');
     cy.get('#L2AGLb').click();
     cy.get('.RNNXgb').type ('vlog de it').type('{enter}');


     cy.get('#rcnt').should('exist')
    } )

   
})
