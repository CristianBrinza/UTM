package Lab3.src;

public final class Store extends Manager {

    public Store(String PharmacyName) {
        super(PharmacyName);
    }

    @Override
    public void printStats() {
        System.out.println("Number of all employees: " + countIds);
        System.out.println("List of id of all employees: " + ids);
    }

}
