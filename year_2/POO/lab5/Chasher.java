public final class Chasher extends Root implements OrderChecker {

    public Chasher ( ) {
        this.id = generateId ( );
    }

    @Override
    public void checkOrder ( boolean orderPresent ) {
        System.out.println ("Chasher with id   [" + this.id + "]   checks if the client with has a recipe");
        if (orderPresent) {
            System.out.println ("Client has the recipe, so librarian with id   [" + this.id + "]   can sell him the book");
        } else {
            System.out.println ("Client doesn't have the recipe, so chasher with id   [" + this.id + "]   can not sell him the product");
        }
    }

    @Override
    public int getId ( ) {
        return this.id;
    }

}
