package domain.patterns.decorator;

import domain.patterns.composite.BookComponent;

// Decorator that adds bonus content feature to a book
public class BonusContentDecorator extends BookDecorator {

    public BonusContentDecorator(BookComponent bookComponent) {
        super(bookComponent);
    }

    @Override
    public double getPrice() {
        return super.getPrice() + 3;  // Additional cost for bonus content
    }

    @Override
    public void printDetails() {
        super.printDetails();
        System.out.println("Feature: Bonus Content");
    }
}
