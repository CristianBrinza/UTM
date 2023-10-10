package factory;

import models.IProduct;
import models.Product;

/**
 * The ProductFactory class is responsible for creating instances of products.
 * It adheres to the Open/Closed Principle (OCP) by being open for extension
 * (to create new types of products) but closed for modification.
 */
public class ProductFactory implements AbstractFactory<IProduct> {
    /**
     * Method to create and return a product instance based on the provided type.
     * @param type The type of the product to create.
     * @return An instance of a product.
     */
    @Override
    public IProduct create(String type) {
        switch (type) {
            case "Electronics":
                return new Product("Electronics Item", 1000.0);
            case "Clothes":
                return new Product("Clothes Item", 500.0);
            default:
                throw new IllegalArgumentException("Unknown product type");
        }
    }
}
