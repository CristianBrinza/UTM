package patterns.creational.abstractFactory.books;

import domain.Product;
import domain.products.books.Book;
import domain.products.books.Magazine;
import patterns.creational.abstractFactory.AbstractProductFactory;

public class BookFactory implements AbstractProductFactory {
    @Override
    public Product createProduct(String type) {
        if (type.equalsIgnoreCase("BOOK")) {
            return new Book("Default Book Name", 45.99);
        } else if (type.equalsIgnoreCase("MAGAZINE")) {
            return new Magazine("Default Magazine Name");
        }
        return null;
    }
}
