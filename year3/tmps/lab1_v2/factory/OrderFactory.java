package factory;

import models.Customer;
import models.IProduct;
import models.Order;

import java.util.List;

/**
 * The OrderFactory class is responsible for creating instances of orders.
 * It adheres to the Open/Closed Principle (OCP) by being open for extension
 * (to create new types of orders) but closed for modification.
 */
public class OrderFactory implements AbstractFactory<Order> {
    /**
     * Method to create and return an order instance based on the provided products and customer.
     * @param args The arguments used for creating an order.
     *             args[0] should be a List<IProduct> representing the products in the order.
     *             args[1] should be a Customer representing the customer who placed the order.
     * @return An instance of an order.
     */
    @Override
    public Order create(Object... args) {
        if (args.length != 2 || !(args[0] instanceof List) || !(args[1] instanceof Customer)) {
            throw new IllegalArgumentException("Invalid arguments for creating Order");
        }
        List<IProduct> products = (List<IProduct>) args[0];
        Customer customer = (Customer) args[1];
        return new Order(products, customer);
    }
}
