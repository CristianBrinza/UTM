package patterns.behavioral.mediator;


// Concrete Colleague for inventory management
public class InventoryComponent extends Component {
    public InventoryComponent(ShoppingMediator mediator) {
        super(mediator);
    }

    public void checkAvailability() {
        System.out.println("Checking product availability.");
        // Check inventory logic
    }

    public void updateInventory() {
        System.out.println("Updating inventory.");
        // Update inventory logic
    }

    @Override
    public void receive(String event) {
        // Handle received events
    }
}

