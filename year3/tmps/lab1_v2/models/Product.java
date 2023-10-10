package models;

/**
 * The Product class represents a product entity in the online shopping domain.
 * It adheres to the Single Responsibility Principle (SRP) by having
 * one reason to change, which is changing the way we represent a product.
 */
public class Product implements IProduct {
    private final String name;
    private final double price;

    /**
     * Constructor to initialize a Product object.
     * @param name  The name of the product.
     * @param price The price of the product.
     */
    public Product(String name, double price) {
        this.name = name;
        this.price = price;
    }

    /**
     * Getter method for the name of the product.
     * @return The name of the product.
     */
    @Override
    public String getName() {
        return name;
    }

    /**
     * Getter method for the price of the product.
     * @return The price of the product.
     */
    @Override
    public double getPrice() {
        return price;
    }
}
