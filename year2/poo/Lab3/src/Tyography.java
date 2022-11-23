package Lab3.src;

public class Tyography extends Manager {

    public Tyography(String CompanyName) {
        super(CompanyName);
    }

    @Override
    public void printStats() {
        System.out.println("Number of all products which belong to this manufacturer: " + countIds);
        System.out.println("List of id of all products of this company: " + ids);
    }

    public void addProduct(int i) {
    }

    public String getProducts() {
        System.out.println("added");
        return null;
    }
}
