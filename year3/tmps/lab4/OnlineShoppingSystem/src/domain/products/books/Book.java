package domain.products.books;

import domain.products.Product;

public class Book implements Product {
    private String name;

    public Book(String name) {
        this.name = name;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public void describeProduct() {
        System.out.println("This is a book named " + name + ".");
    }

    @Override
    public Product cloneProduct() {
        return null;
    }
}
