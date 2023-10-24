package domain.patterns.composite;

import java.util.ArrayList;
import java.util.List;

// Represents a collection of books or other collections and implements the BookComponent interface
public class BookCollection implements BookComponent {
    private String name;
    private List<BookComponent> components;

    public BookCollection(String name) {
        this.name = name;
        this.components = new ArrayList<>();
    }

    public void addComponent(BookComponent component) {
        components.add(component);
    }

    @Override
    public double getPrice() {
        double total = 0.0;
        for (BookComponent component : components) {
            total += component.getPrice();
        }
        return total;
    }

    @Override
    public void printDetails() {
        System.out.println("Book Collection: " + name);
        for (BookComponent component : components) {
            component.printDetails();
        }
    }
}
