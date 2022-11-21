public class Librarian extends Root {

    public Librarian ( ) {
        this.id = generateId ( );
    }

    public void sellBook ( CostumerInterface patient , BookInterface product ) {
        patient.addBook (product.getId ( ));
        System.out.println (" ");
        System.out.println ("The Librarian with id   [" + this.id + "]   createt the recipe with id   [" +
                product.getId ( ) + "]   to the customer with id   [" + patient.getId ( )+"]");
    }


}
