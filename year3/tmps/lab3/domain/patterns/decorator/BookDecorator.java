package domain.patterns.decorator;

import domain.patterns.composite.BookComponent;

// Abstract decorator class that implements BookComponent
public abstract class BookDecorator implements BookComponent {
    protected BookComponent bookComponent;

    public BookDecorator(BookComponent bookComponent) {
        this.bookComponent = bookComponent;
    }

    @Override
    public double getPrice() {
        return bookComponent.getPrice();
    }

    @Override
    public void printDetails() {
        bookComponent.printDetails();
    }
}
