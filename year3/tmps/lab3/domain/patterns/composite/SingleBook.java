package domain.patterns.composite;

import domain.models.Book;

// Represents individual books and implements the BookComponent interface
public class SingleBook implements BookComponent {
    private Book book;

    public SingleBook(Book book) {
        this.book = book;
    }

    @Override
    public double getPrice() {
        return book.getPrice();
    }

    @Override
    public void printDetails() {
        System.out.println("Single Book: " + book.getTitle() + ", Author: " + book.getAuthor().getName() + ", Price: " + book.getPrice());
    }
}
