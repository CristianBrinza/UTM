package domain.patterns.composite;

import java.util.ArrayList;
import java.util.List;

/**
 * Represents a collection of books or other collections and implements the BookComponent interface.
 * This class is a composite object in the Composite pattern, meaning it can contain other BookComponent objects.
 */
public class BookCollection implements BookComponent {
    private String name;  // Name of the collection
    private List<BookComponent> components;  // List of components, can be other collections or individual books

    /**
     * Constructor for BookCollection.
     * 
     * @param name Name of the collection.
     */
    public BookCollection(String name) {
        this.name = name;
        this.components = new ArrayList<>();
    }

    /**
     * Adds a BookComponent (either SingleBook or another BookCollection) to this collection.
     * 
     * @param component The component to be added to the collection.
     */
    public void addComponent(BookComponent component) {
        components.add(component);
    }

    /**
     * Returns the total price of all components in the collection.
     * 
     * @return Total price of the collection.
     */
    @Override
    public double getPrice() {
        double total = 0.0;
        for (BookComponent component : components) {
            total += component.getPrice();
        }
        return total;
    }

    /**
     * Prints the details of the entire collection.
     */
    @Override
    public void printDetails() {
        System.out.println("Book Collection: " + name);
        for (BookComponent component : components) {
            component.printDetails();
        }
    }
}