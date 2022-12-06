package model;

public final class Librarian extends Root implements OrderChecker {

    public Librarian() {
        this.id = generateId();
    }

    @Override
    public void checkOrder(boolean orederPresent) {
        System.out.println("Librarian with id " + this.id + " checks if the client with has a order");
        if (orederPresent) {
            System.out.println("Client has the order, so Librarian with id " + this.id + " can sell him the product");
        } else {
            System.out.println("Client doesn't have the order, so Librarian with id " + this.id + " can not sell him the product");
        }
    }

    @Override
    public int getId() {
        return this.id;
    }
}
