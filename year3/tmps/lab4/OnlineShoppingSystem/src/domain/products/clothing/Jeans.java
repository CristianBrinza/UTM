package domain.products.clothing;
import domain.Product;
public class Jeans implements Product {
    private String name;

    public Jeans(String name) {
        this.name = name;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public String getDescription() {
        return null;
    }

    @Override
    public double getPrice() {
        return 0;
    }

    @Override
    public void describeProduct() {
        System.out.println("This is a pair of Jeans named " + name + ".");
    }

    @Override
    public Product cloneProduct() {
        return null;
    }
}

