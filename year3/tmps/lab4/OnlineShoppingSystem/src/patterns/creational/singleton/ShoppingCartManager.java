package patterns.creational.singleton;

import domain.Product;

import java.util.ArrayList;
import java.util.List;

public class ShoppingCartManager {
    private static ShoppingCartManager instance;
    private List<Product> cartProducts;

    private ShoppingCartManager() {
        cartProducts = new ArrayList<>();
    }

    public static synchronized ShoppingCartManager getInstance() {
        if (instance == null) {
            instance = new ShoppingCartManager();
        }
        return instance;
    }

    public void addProductToCart(Product product) {
        cartProducts.add(product);
        System.out.println(product.getName() + " added to the cart.");
    }

    public void removeProductFromCart(Product product) {
        if(cartProducts.remove(product)) {
            System.out.println(product.getName() + " removed from the cart.");
        } else {
            System.out.println("Product not found in the cart.");
        }
    }

    public void displayCart() {
        if(cartProducts.isEmpty()) {
            System.out.println("The shopping cart is empty.");
        } else {
            System.out.println("Shopping Cart Contents:");
            for (Product product : cartProducts) {
                System.out.println("- " + product.getName());
            }
        }
    }
}

