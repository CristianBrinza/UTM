package domain.patterns.composite;

/**
 * Interface representing the component for both individual books and collections.
 * This interface sets a contract for both the composite (BookCollection) and leaf (SingleBook) objects.
 */
public interface BookComponent {
    /**
     * Returns the price of the book or the total price of the collection.
     * 
     * @return Price of the book or total price of the collection.
     */
    double getPrice();

    /**
     * Prints the details of the book or the details of the entire collection.
     */
    void printDetails();
}