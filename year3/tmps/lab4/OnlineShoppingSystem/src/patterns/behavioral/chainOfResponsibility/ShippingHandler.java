package patterns.behavioral.chainOfResponsibility;


import domain.Order;

// Concrete Handler for arranging shipping
public class ShippingHandler implements OrderHandler {
    private OrderHandler nextHandler;

    @Override
    public void setNextHandler(OrderHandler nextHandler) {
        this.nextHandler = nextHandler;
    }

    @Override
    public void process(Order order) {
        System.out.println("Arranging shipping for the order.");
        // Shipping logic

        if (nextHandler != null) {
            nextHandler.process(order);
        }
    }
}

