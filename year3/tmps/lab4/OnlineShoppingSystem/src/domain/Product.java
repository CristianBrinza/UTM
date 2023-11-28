package domain;

public interface Product {
    String getName();
    String getDescription();
    double getPrice();
    void describeProduct();
    Product cloneProduct(); // Method to clone the product
}
