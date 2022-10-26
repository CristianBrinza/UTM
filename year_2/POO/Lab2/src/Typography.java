package Lab2.src;

import java.util.ArrayList;

public class Typography {
    public static int NumberOfTypogrphies = 0;
    private int id;
    private String name;
    private int numberOfProducts = 0;
    private ArrayList<Integer> products = new ArrayList<Integer>();

    public Typography(String CompanyName) {
        NumberOfTypogrphies += 1;
        this.name = CompanyName;
        this.id = generateTypographyId();
    }

    private int generateTypographyId() {
        return (int) ((Math.random() * (99999 - 10000)) + 10000);
    }

    public void addBook(int productId) {
        products.add(productId);
        numberOfProducts += 1;
    }

    public String getName() {
        return this.name;
    }

    public int getId() {
        return this.id;
    }

    public int getNumberOfProducts() {
        return this.numberOfProducts;
    }

    public ArrayList getProducts() {
        return this.products;
    }

}
