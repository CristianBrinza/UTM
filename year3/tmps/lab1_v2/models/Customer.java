package models;

/**
 * The Customer class represents a customer entity in the online shopping domain.
 * It adheres to the Single Responsibility Principle (SRP) by having
 * one reason to change, which is changing the way we represent a customer.
 */
public class Customer {
    private final String name;
    private final String email;

    /**
     * Constructor to initialize a Customer object.
     * @param name  The name of the customer.
     * @param email The email address of the customer.
     */
    public Customer(String name, String email) {
        if (name == null || name.trim().isEmpty()) {
            throw new IllegalArgumentException("Customer name cannot be empty.");
        }
        if (email == null || email.trim().isEmpty()) {
            throw new IllegalArgumentException("Customer email cannot be empty.");
        }
        this.name = name;
        this.email = email;
    }

    /**
     * Getter method for the name of the customer.
     * @return The name of the customer.
     */
    public String getName() {
        return name;
    }

    /**
     * Getter method for the email address of the customer.
     * @return The email address of the customer.
     */
    public String getEmail() {
        return email;
    }
}
