package patterns.structural.composite;


// Leaf: Represents individual objects in the composition.
public class ProductLeaf extends ProductComponent {
    private String name;
    private double price;

    public ProductLeaf(String name, double price) {
        this.name = name;
        this.price = price;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public double getPrice() {
        return price;
    }

    @Override
    public void displayProductInfo() {
        System.out.println("Product: " + getName() + ", Price: " + getPrice());
    }
}
