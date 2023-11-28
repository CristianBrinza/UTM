package patterns.structural.facade;


import subsystems.InventoryManager;
import subsystems.PaymentGateway;
import subsystems.ShippingService;

public class ShoppingFacade {
    private InventoryManager inventoryManager;
    private PaymentGateway paymentGateway;
    private ShippingService shippingService;

    public ShoppingFacade() {
        inventoryManager = new InventoryManager();
        paymentGateway = new PaymentGateway();
        shippingService = new ShippingService();
    }

    public void completeOrder(String productID, int quantity, String paymentDetails, String address) {
        paymentGateway.processPayment(paymentDetails);
        inventoryManager.updateInventory(productID, quantity);
        shippingService.scheduleDelivery(address);
        System.out.println("Order completed successfully.");
    }
}

