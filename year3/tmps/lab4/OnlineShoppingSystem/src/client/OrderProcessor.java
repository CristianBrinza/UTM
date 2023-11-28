package client;



import domain.Order;
import patterns.behavioral.chainOfResponsibility.*;

// Client code to demonstrate the Chain of Responsibility pattern
public class OrderProcessor {
    public static void main(String[] args) {
        OrderHandler inventoryCheck = new InventoryCheckHandler();
        OrderHandler paymentProcessing = new PaymentProcessingHandler();
        OrderHandler shipping = new ShippingHandler();

        // Setting up the chain
        inventoryCheck.setNextHandler(paymentProcessing);
        paymentProcessing.setNextHandler(shipping);

        // Create an order
        Order order = new Order();
        // Process the order through the chain
        inventoryCheck.process(order);
    }
}

