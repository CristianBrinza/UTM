package patterns.creational.prototype;

import java.util.List;
import java.util.ArrayList;

import domain.Product;

// Concrete Prototype: Implements the Prototype interface for cloning shopping cart.
public class ConcreteShoppingCartPrototype implements ShoppingCartPrototype {
    private List<Product> products;

    public ConcreteShoppingCartPrototype() {
        this.products = new ArrayList<>();
    }

    public void addProduct(Product product) {
        products.add(product);
    }

    @Override
    public ShoppingCartPrototype cloneCart() {
        ConcreteShoppingCartPrototype newCart = new ConcreteShoppingCartPrototype();
        for (Product product : this.products) {
            // Assume Product also implements a cloning method or has a copy constructor
            newCart.addProduct(product.cloneProduct());
        }
        return newCart;
    }

    public void displayCartContents() {
        System.out.println("Shopping Cart Contents:");
        for (Product product : products) {
            System.out.println(product.getName());
        }
    }
}

