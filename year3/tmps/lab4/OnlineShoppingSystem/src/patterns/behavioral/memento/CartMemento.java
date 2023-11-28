package patterns.behavioral.memento;


import java.util.ArrayList;
import java.util.List;
import domain.products.Product;

// Memento class
public class CartMemento {
    private List<Product> products;

    public CartMemento(List<Product> products) {
        this.products = new ArrayList<>(products);
    }

    List<Product> getSavedState() {
        return products;
    }
}

