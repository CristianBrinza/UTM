package client;

import domain.products.Product;
import domain.products.books.Book;
import domain.products.books.Magazine;
import domain.products.electronics.Electronics;
import domain.products.electronics.Gadget;
import domain.products.payment.PaymentProcessor;
import domain.products.payment.ThirdPartyPaymentProcessor;
import patterns.creational.singleton.ShoppingCartManager;
import patterns.structural.adapter.PaymentAdapter;
import patterns.structural.bridge.MobileAppInterface;
import patterns.structural.bridge.UserInterfaceBridge;
import patterns.structural.bridge.WebInterface;

public class ShoppingCart {
    public static void main(String[] args) {
        ShoppingCartManager cartManager = ShoppingCartManager.getInstance();

        Product book = new Book("Java Design Patterns");
        Product magazine = new Magazine("The Magazine of Modern Tech");
        Product electronic = new Electronics("Smartphone");
        Product gadget = new Gadget("Smartwatch");

        cartManager.addProductToCart(book);
        cartManager.addProductToCart(magazine);
        cartManager.addProductToCart(electronic);
        cartManager.addProductToCart(gadget);

        cartManager.displayCart();

        cartManager.removeProductFromCart(magazine);
        cartManager.displayCart();



        // Adapter pattern demonstration
        PaymentProcessor paymentProcessor = new PaymentAdapter(new ThirdPartyPaymentProcessor());
        paymentProcessor.processPayment(100.0); // Using the adapter to process the payment

        // Bridge pattern demonstration
        UserInterfaceBridge webUI = new UserInterfaceBridge(new WebInterface());
        webUI.showProduct("Book: Design Patterns");

        UserInterfaceBridge mobileUI = new UserInterfaceBridge(new MobileAppInterface());
        mobileUI.showProduct("Gadget: Smartwatch");

    }
}
