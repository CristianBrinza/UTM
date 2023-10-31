package domain.patterns.decorator;

import domain.patterns.composite.BookComponent;

/**
 * Concrete decorator that adds hardcover feature to a book.
 */
public class HardcoverDecorator extends BookDecorator {

    /**
     * Constructor for HardcoverDecorator.
     * 
     * @param bookComponent Component to be decorated.
     */
    public HardcoverDecorator(BookComponent bookComponent) {
        super(bookComponent);
    }

    /**
     * Returns the price of the book with the additional cost for hardcover.
     * 
     * @return Price of the book with hardcover.
     */
    @Override
    public double getPrice() {
        return super.getPrice() + 10;  // Additional cost for hardcover
    }

    /**
     * Prints the details of the book along with the hardcover feature.
     */
    @Override
    public void printDetails() {
        super.printDetails();
        System.out.println("Feature: Hardcover");
    }
}