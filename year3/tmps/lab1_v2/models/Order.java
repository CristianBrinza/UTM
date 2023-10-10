package models;

import models.Customer;

import java.util.List;

/**
 * The models.Order class represents an order entity in the online shopping domain.
 * It adheres to the Single Responsibility Principle (SRP) by having
 * one reason to change, which is changing the way we represent an order.
 */
public class Order {
    private final List<IProduct> products;
    private final Customer customer;

    /**
     * Constructor to initialize an models.Order object.
     * @param products  The list of products in the order.
     * @param customer The customer who placed the order.
     */
    public Order(List<IProduct> products, Customer customer) {
        if (products == null || products.isEmpty()) {
            throw new IllegalArgumentException("models.Order must have at least one product.");
        }
        this.products = products;
        this.customer = customer;
    }

    /**
     * Getter method for the products in the order.
     * @return The list of products.
     */
    public List<IProduct> getProducts() {
        return products;
    }

    /**
     * Getter method for the customer who placed the order.
     * @return The customer.
     */
    public Customer getCustomer() {
        return customer;
    }

    /**
     * Method to calculate and return the total price of the order.
     * @return The total price of products in the order.
     */
    public double calculateTotal() {
        return products.stream().mapToDouble(IProduct::getPrice).sum();
    }
}
