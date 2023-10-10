package domain;

import models.IProduct;
import java.util.ArrayList;
import java.util.List;

/**
 * The ShoppingCart class manages products in an online shopping domain.
 * It adheres to the Single Responsibility Principle (SRP) by having
 * one reason to change, which is changing the way we manage products in the cart.
 */
public class ShoppingCart {
    private final List<IProduct> products;

    /**
     * Constructor to initialize a ShoppingCart object.
     */
    public ShoppingCart() {
        this.products = new ArrayList<>();
    }

    /**
     * Method to add a product to the shopping cart.
     * @param product The product to be added to the cart.
     */
    public void addProduct(IProduct product) {
        products.add(product);
    }

    /**
     * Method to calculate and return the total price of all products in the cart.
     * @return The total price of products.
     */
    public double calculateTotal() {
        return products.stream().mapToDouble(IProduct::getPrice).sum();
    }
}
