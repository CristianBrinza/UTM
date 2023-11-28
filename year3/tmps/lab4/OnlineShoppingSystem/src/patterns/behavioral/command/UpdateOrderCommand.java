package patterns.behavioral.command;


import domain.Order;

// Concrete Command for updating an order
public class UpdateOrderCommand implements OrderCommand {
    private Order order;

    public UpdateOrderCommand(Order order) {
        this.order = order;
    }

    @Override
    public void execute() {
        order.update();
    }
}

