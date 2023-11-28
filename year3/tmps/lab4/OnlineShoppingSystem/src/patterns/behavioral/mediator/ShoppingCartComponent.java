package patterns.behavioral.mediator;


// Concrete Colleague for shopping cart
public class ShoppingCartComponent extends Component {
    public ShoppingCartComponent(ShoppingMediator mediator) {
        super(mediator);
    }

    public void checkout() {
        System.out.println("Initiating checkout process.");
        send("CHECKOUT");
    }

    public void clearCart() {
        System.out.println("Clearing shopping cart.");
        // Clear cart logic
    }

    @Override
    public void receive(String event) {
        // Handle received events
    }
}

