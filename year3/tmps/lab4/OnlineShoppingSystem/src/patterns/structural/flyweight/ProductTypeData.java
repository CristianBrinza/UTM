package patterns.structural.flyweight;


// Concrete Flyweight class storing intrinsic data (shared)
public class ProductTypeData implements ProductFlyweight {
    private String category;
    private double discountRate;
    private String brand;

    public ProductTypeData(String category, double discountRate, String brand) {
        this.category = category;
        this.discountRate = discountRate;
        this.brand = brand;
    }

    @Override
    public void displayProductTypeData() {
        System.out.println("Category: " + category + ", Discount: " + discountRate + "%, Brand: " + brand);
    }
}
