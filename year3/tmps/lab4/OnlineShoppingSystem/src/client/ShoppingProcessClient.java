package client;


import patterns.behavioral.mediator.*;

// Client code to demonstrate Mediator Pattern
public class ShoppingProcessClient {
    public static void main(String[] args) {
        ShoppingMediator mediator = new ConcreteShoppingMediator();
        ShoppingCartComponent cart = new ShoppingCartComponent(mediator);
        PaymentComponent payment = new PaymentComponent(mediator);
        InventoryComponent inventory = new InventoryComponent(mediator);

        ((ConcreteShoppingMediator) mediator).registerShoppingCart(cart);
        ((ConcreteShoppingMediator) mediator).registerPayment(payment);
        ((ConcreteShoppingMediator) mediator).registerInventory(inventory);

        // Simulating shopping process
        cart.checkout();
        payment.processPayment();
    }
}
