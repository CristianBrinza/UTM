package patterns.behavioral.chainOfResponsibility;


import domain.Order;

// Concrete Handler for checking inventory
public class InventoryCheckHandler implements OrderHandler {
    private OrderHandler nextHandler;

    @Override
    public void setNextHandler(OrderHandler nextHandler) {
        this.nextHandler = nextHandler;
    }

    @Override
    public void process(Order order) {
        System.out.println("Checking inventory for the order.");
        // Inventory check logic

        if (nextHandler != null) {
            nextHandler.process(order);
        }
    }
}

