package patterns.behavioral.chainOfResponsibility;

import domain.Order;

// Concrete Handler for processing payment
public class PaymentProcessingHandler implements OrderHandler {
    private OrderHandler nextHandler;

    @Override
    public void setNextHandler(OrderHandler nextHandler) {
        this.nextHandler = nextHandler;
    }

    @Override
    public void process(Order order) {
        System.out.println("Processing payment for the order.");
        // Payment processing logic

        if (nextHandler != null) {
            nextHandler.process(order);
        }
    }
}

