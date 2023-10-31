package domain.patterns.decorator;

import domain.patterns.composite.BookComponent;

/**
 * Abstract decorator class that implements the BookComponent interface.
 * It serves as a base class for all concrete decorators that want to 
 * add additional features to books.
 */
public abstract class BookDecorator implements BookComponent {
    protected BookComponent bookComponent;  // Reference to the component being decorated

    /**
     * Constructor for BookDecorator.
     * 
     * @param bookComponent Component to be decorated.
     */
    public BookDecorator(BookComponent bookComponent) {
        this.bookComponent = bookComponent;
    }

    /**
     * Returns the price of the book.
     * 
     * @return Price of the book.
     */
    @Override
    public double getPrice() {
        return bookComponent.getPrice();
    }

    /**
     * Prints the details of the book.
     */
    @Override
    public void printDetails() {
        bookComponent.printDetails();
    }
}