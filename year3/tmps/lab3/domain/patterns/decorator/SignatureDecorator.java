package domain.patterns.decorator;

import domain.patterns.composite.BookComponent;

/**
 * Concrete decorator that adds author's signature feature to a book.
 */
public class SignatureDecorator extends BookDecorator {

    /**
     * Constructor for SignatureDecorator.
     * 
     * @param bookComponent Component to be decorated.
     */
    public SignatureDecorator(BookComponent bookComponent) {
        super(bookComponent);
    }

    /**
     * Returns the price of the book with the additional cost for author's signature.
     * 
     * @return Price of the book with author's signature.
     */
    @Override
    public double getPrice() {
        return super.getPrice() + 5;  // Additional cost for author's signature
    }

    /**
     * Prints the details of the book along with the author's signature feature.
     */
    @Override
    public void printDetails() {
        super.printDetails();
        System.out.println("Feature: Author's Signature");
    }
}