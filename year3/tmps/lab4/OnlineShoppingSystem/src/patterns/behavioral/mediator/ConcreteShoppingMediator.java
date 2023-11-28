package patterns.behavioral.mediator;


// Concrete Mediator
public class ConcreteShoppingMediator implements ShoppingMediator {
    private ShoppingCartComponent shoppingCart;
    private PaymentComponent payment;
    private InventoryComponent inventory;

    public void registerShoppingCart(ShoppingCartComponent shoppingCart) {
        this.shoppingCart = shoppingCart;
    }

    public void registerPayment(PaymentComponent payment) {
        this.payment = payment;
    }

    public void registerInventory(InventoryComponent inventory) {
        this.inventory = inventory;
    }

    @Override
    public void handle(String event, Component component) {
        switch (event) {
            case "CHECKOUT":
                inventory.checkAvailability();
                break;
            case "PAYMENT_SUCCESSFUL":
                shoppingCart.clearCart();
                inventory.updateInventory();
                break;
            // Additional cases for other events
        }
    }
}

