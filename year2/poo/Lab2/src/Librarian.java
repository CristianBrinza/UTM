package Lab2.src;

public class Librarian {

    private int id;
    private String name;

    public Librarian(String name) {
        this.id = generateLibratianId();
        this.name = name;
    }

    private int generateLibratianId() {
        return (int) ((Math.random() * (99999 - 10000)) + 10000);
    }

    public void sellBook(int bookId, int customerId) {
        System.out.println("The doctor with id " + this.id
                + " to the customer with id " + customerId);
    }

    public int getId() {
        return this.id;
    }

    public String getName() {
        return name;
    }

}
