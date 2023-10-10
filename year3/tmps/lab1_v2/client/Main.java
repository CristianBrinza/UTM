package client;
import domain.ShoppingCart;
import factory.CustomerFactory;
import factory.OrderFactory;
import factory.ProductFactory;
import models.Customer;
import models.IProduct;
import models.Order;

import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        // Instantiate factories
        ProductFactory productFactory = new ProductFactory();
        CustomerFactory customerFactory = new CustomerFactory();
        OrderFactory orderFactory = new OrderFactory();

        // Create products
        IProduct electronics = productFactory.create("Electronics");
        IProduct clothes = productFactory.create("Clothes");
        List<IProduct> products = Arrays.asList(electronics, clothes);

        // Create customer
        Customer customer = customerFactory.create("John Doe", "john@example.com");

        // Create order
        Order order = orderFactory.create(products, customer);

        // Output
        System.out.println("Order Total: " + order.calculateTotal());
        System.out.println("Customer Name: " + order.getCustomer().getName());
    }
}
