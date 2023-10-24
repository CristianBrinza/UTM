package domain.patterns.decorator;

import domain.patterns.composite.BookComponent;

// Decorator that adds hardcover feature to a book
public class HardcoverDecorator extends BookDecorator {

    public HardcoverDecorator(BookComponent bookComponent) {
        super(bookComponent);
    }

    @Override
    public double getPrice() {
        return super.getPrice() + 10;  // Additional cost for hardcover
    }

    @Override
    public void printDetails() {
        super.printDetails();
        System.out.println("Feature: Hardcover");
    }
}
