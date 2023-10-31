package domain.patterns.decorator;

import domain.patterns.composite.BookComponent;

/**
 * Concrete decorator that adds bonus content feature to a book.
 */
public class BonusContentDecorator extends BookDecorator {

    /**
     * Constructor for BonusContentDecorator.
     * 
     * @param bookComponent Component to be decorated.
     */
    public BonusContentDecorator(BookComponent bookComponent) {
        super(bookComponent);
    }

    /**
     * Returns the price of the book with the additional cost for bonus content.
     * 
     * @return Price of the book with bonus content.
     */
    @Override
    public double getPrice() {
        return super.getPrice() + 3;  // Additional cost for bonus content
    }

    /**
     * Prints the details of the book along with the bonus content feature.
     */
    @Override
    public void printDetails() {
        super.printDetails();
        System.out.println("Feature: Bonus Content");
    }
}