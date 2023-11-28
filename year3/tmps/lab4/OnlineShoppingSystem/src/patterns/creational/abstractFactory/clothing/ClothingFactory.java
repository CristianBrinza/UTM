package patterns.creational.abstractFactory.clothing;

import domain.Product;
import domain.products.clothing.Jeans;
import domain.products.clothing.TShirt;
import patterns.creational.abstractFactory.AbstractProductFactory;

// Clothing Factory: Implements the Abstract Factory interface to create clothing products.
// Clothing Factory: Creates clothing products.
public class ClothingFactory implements AbstractProductFactory {
    @Override
    public Product createProduct(String type) {
        if (type.equalsIgnoreCase("TSHIRT")) {
            return new TShirt("Default T-Shirt");
        } else if (type.equalsIgnoreCase("JEANS")) {
            return new Jeans("Default Jeans");
        }
        return null;
    }
}


