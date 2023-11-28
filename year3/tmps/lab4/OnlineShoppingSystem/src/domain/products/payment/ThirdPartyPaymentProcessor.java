package domain.products.payment;


// Third-party payment processor with a different interface
public class ThirdPartyPaymentProcessor {
    public void executeTransaction(double amount) {
        System.out.println("Processing payment of $" + amount + " through third-party processor.");
        // Logic for third-party payment processing
    }
}
