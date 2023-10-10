package factory;

import models.Customer;

import models.Customer;

/**
 * The CustomerFactory class is responsible for creating instances of customers.
 * It adheres to the Open/Closed Principle (OCP) by being open for extension
 * (to create new types of customers) but closed for modification.
 */
public class CustomerFactory implements AbstractFactory<Customer> {
    /**
     * Method to create and return a customer instance based on the provided name and email.
     * @param args The arguments used for creating a customer.
     *             args[0] should be a String representing the name of the customer.
     *             args[1] should be a String representing the email address of the customer.
     * @return An instance of a customer.
     */
    @Override
    public Customer create(Object... args) {
        if (args.length != 2 || !(args[0] instanceof String) || !(args[1] instanceof String)) {
            throw new IllegalArgumentException("Invalid arguments for creating Customer");
        }
        String name = (String) args[0];
        String email = (String) args[1];
        return new Customer(name, email);
    }
}
