package domain.patterns.composite;

import domain.models.Book;

/**
 * Represents individual books and implements the BookComponent interface.
 * This class is a leaf in the Composite pattern, meaning it doesn't contain any other components.
 */
public class SingleBook implements BookComponent {
    private Book book;  // The actual book object

    /**
     * Constructor for SingleBook.
     * 
     * @param book The actual book object.
     */
    public SingleBook(Book book) {
        this.book = book;
    }

    /**
     * Returns the price of the individual book.
     * 
     * @return Price of the book.
     */
    @Override
    public double getPrice() {
        return book.getPrice();
    }

    /**
     * Prints the details of the individual book.
     */
    @Override
    public void printDetails() {
        System.out.println("Single Book: " + book.getTitle() + ", Author: " + book.getAuthor().getName() + ", Price: " + book.getPrice());
    }
}