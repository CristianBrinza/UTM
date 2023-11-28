package patterns.creational.abstractFactory;

import domain.Product;

// Abstract Factory Interface: Defines methods for creating different abstract product types.
// Each concrete factory implementing this interface will create products of a specific category.
public interface AbstractProductFactory {
    Product createProduct(String type);
}



