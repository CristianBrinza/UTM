package Lab3.src;

public class Librarian extends Costumer {

    public Librarian(String name) {
        super(name);
    }

    public void prescribeDrug(int drugId, int customerId) {
        System.out.println("The doctor with id " + this.id + " prescribed the drug with id + " + drugId
                + " to the customer with id " + customerId);
    }

}
