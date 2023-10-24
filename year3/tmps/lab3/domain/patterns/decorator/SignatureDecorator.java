package domain.patterns.decorator;

import domain.patterns.composite.BookComponent;

// Decorator that adds author's signature feature to a book
public class SignatureDecorator extends BookDecorator {

    public SignatureDecorator(BookComponent bookComponent) {
        super(bookComponent);
    }

    @Override
    public double getPrice() {
        return super.getPrice() + 5;  // Additional cost for author's signature
    }

    @Override
    public void printDetails() {
        super.printDetails();
        System.out.println("Feature: Author's Signature");
    }
}
