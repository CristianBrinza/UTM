package domain.products;

public interface Product {
    String getName();
    void describeProduct();
    Product cloneProduct(); // Method to clone the product
}

