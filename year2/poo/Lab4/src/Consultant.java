package src;

public class Consultant extends Root {

    public Consultant() {
        this.id = generateId();
    }

    public void suggestbook(ClientInterface patient, ProductInterface product) {
        patient.addOrder(product.getId());
        System.out.println(" ");
        System.out.println("The Consultant with id " + this.id + " suggested the book with id " + product.getId() + " to the customer with id " + patient.getId());
    }
}
