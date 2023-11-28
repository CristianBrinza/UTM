package patterns.creational.factoryMethod;

import domain.Product;
import domain.products.books.Book;
import domain.products.electronics.Electronics;
// Factory Method: Provides a method for creating objects, allowing subclasses to alter the type of objects that will be created.
public class ProductFactory {
    public static Product getProduct(String productType) {
        if (productType == null) {
            return null;
        }
        if (productType.equalsIgnoreCase("BOOK")) {
            return new Book("Default Book", 45.99);
        } else if (productType.equalsIgnoreCase("ELECTRONICS")) {
            return new Electronics("Default Electronics");
        }
        return null;
    }
}


