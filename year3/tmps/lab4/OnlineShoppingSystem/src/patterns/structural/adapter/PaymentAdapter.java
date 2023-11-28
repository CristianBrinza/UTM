package patterns.structural.adapter;



import domain.products.payment.PaymentProcessor;
import domain.products.payment.ThirdPartyPaymentProcessor;


// Adapter class: Adapts ThirdPartyPaymentProcessor to PaymentProcessor interface
public class PaymentAdapter implements PaymentProcessor {
    private ThirdPartyPaymentProcessor thirdPartyProcessor;

    public PaymentAdapter(ThirdPartyPaymentProcessor thirdPartyProcessor) {
        this.thirdPartyProcessor = thirdPartyProcessor;
    }

    @Override
    public void processPayment(double amount) {
        thirdPartyProcessor.executeTransaction(amount); // Delegates the call to the third-party processor
    }
}
