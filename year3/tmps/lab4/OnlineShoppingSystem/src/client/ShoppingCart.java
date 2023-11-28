package client;

import domain.Order;
import domain.Product;
import domain.products.ProductDetail;
import domain.products.books.Book;
import domain.products.books.Magazine;
import domain.products.electronics.Electronics;
import domain.products.electronics.Gadget;
import domain.products.payment.PaymentProcessor;
import domain.products.payment.ThirdPartyPaymentProcessor;
import patterns.behavioral.command.*;
import patterns.creational.singleton.ShoppingCartManager;
import patterns.structural.adapter.PaymentAdapter;
import patterns.structural.bridge.MobileAppInterface;
import patterns.structural.bridge.UserInterfaceBridge;
import patterns.structural.bridge.WebInterface;
import patterns.structural.composite.ProductComponent;
import patterns.structural.composite.ProductComposite;
import patterns.structural.composite.ProductLeaf;
import patterns.structural.decorator.GiftWrappedProduct;
import patterns.structural.decorator.InsuredProduct;
import patterns.structural.facade.ShoppingFacade;
import patterns.structural.flyweight.ProductFlyweightFactory;

public class ShoppingCart {
    public static void main(String[] args) {

        ShoppingCartManager cartManager = ShoppingCartManager.getInstance();

        Product book = new Book("Java Design Patterns", 45.99);
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


        // Composite pattern demonstration
        ProductComponent bookCategory = new ProductComposite("Books");
        bookCategory.add(new ProductLeaf("Design Patterns", 45.99));
        bookCategory.add(new ProductLeaf("Clean Code", 39.99));

        ProductComponent gadgetCategory = new ProductComposite("Gadgets");
        gadgetCategory.add(new ProductLeaf("Smartwatch", 199.99));
        gadgetCategory.add(new ProductLeaf("Smartphone", 999.99));

        ProductComponent allProducts = new ProductComposite("All Products");
        allProducts.add(bookCategory);
        allProducts.add(gadgetCategory);

        allProducts.displayProductInfo();


        // Decorator pattern demonstration
        Product giftWrappedBook = new GiftWrappedProduct(book);
        Product insuredGiftWrappedBook = new InsuredProduct(giftWrappedBook);

        System.out.println(insuredGiftWrappedBook.getDescription());
        System.out.println("Total Price: $" + insuredGiftWrappedBook.getPrice());


        // Facade pattern demonstration
        ShoppingFacade shoppingFacade = new ShoppingFacade();
        shoppingFacade.completeOrder("12345", 1, "Credit Card", "123 Main St");


        // Flyweight pattern demonstration
        var electronicsData = ProductFlyweightFactory.getProductTypeData("Electronics", 10.0, "XYZ Brand");
        var gadgetData = ProductFlyweightFactory.getProductTypeData("Gadgets", 5.0, "ABC Brand");

        ProductDetail phone = new ProductDetail("Smartphone", 999.99, electronicsData);
        ProductDetail tablet = new ProductDetail("Tablet", 499.99, electronicsData);  // Reusing electronicsData flyweight
        ProductDetail smartWatch = new ProductDetail("Smartwatch", 199.99, gadgetData);

        phone.displayProductInfo();
        tablet.displayProductInfo();
        smartWatch.displayProductInfo();





        Order order = new Order();

        // Create commands
        OrderCommand placeOrder = new PlaceOrderCommand(order);
        OrderCommand updateOrder = new UpdateOrderCommand(order);
        OrderCommand cancelOrder = new CancelOrderCommand(order);

        // Invoker
        OrderCommandInvoker invoker = new OrderCommandInvoker(placeOrder);
        invoker.executeCommand(); // Place order

        invoker = new OrderCommandInvoker(updateOrder);
        invoker.executeCommand(); // Update order

        invoker = new OrderCommandInvoker(cancelOrder);
        invoker.executeCommand(); // Cancel order


    }

    public void addProduct(domain.products.Product laptop) {
    }

    public void displayProducts() {
    }
}
