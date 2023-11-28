package patterns.behavioral.mediator;


// Concrete Colleague for payment processing
public class PaymentComponent extends Component {
    public PaymentComponent(ShoppingMediator mediator) {
        super(mediator);
    }

    public void processPayment() {
        System.out.println("Processing payment.");
        send("PAYMENT_SUCCESSFUL");
    }

    @Override
    public void receive(String event) {
        // Handle received events
    }
}

