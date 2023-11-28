package patterns.behavioral.memento;


import java.util.ArrayList;
import java.util.List;
import domain.products.Product;

// Originator class
public class ShoppingCart {
    private List<Product> products = new ArrayList<>();

    public void addProduct(Product product) {
        products.add(product);
    }

    // Saves the current state
    public CartMemento save() {
        return new CartMemento(products);
    }

    // Restores the saved state
    public void restore(CartMemento memento) {
        products = memento.getSavedState();
    }

    public void displayProducts() {
        for (Product product : products) {
            System.out.println(product.getName());
        }
    }
}

