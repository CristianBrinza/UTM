package patterns.behavioral.command;

// Invoker class
public class OrderCommandInvoker {
    private OrderCommand command;

    public OrderCommandInvoker(OrderCommand command) {
        this.command = command;
    }

    public void executeCommand() {
        command.execute();
    }
}

