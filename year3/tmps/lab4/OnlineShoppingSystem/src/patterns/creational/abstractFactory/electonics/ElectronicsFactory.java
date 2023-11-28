package patterns.creational.abstractFactory.electonics;

import domain.Product;
import domain.products.electronics.Electronics;
import domain.products.electronics.Gadget;
import patterns.creational.abstractFactory.AbstractProductFactory;

public class ElectronicsFactory implements AbstractProductFactory {
    @Override
    public Product createProduct(String type) {
        if (type.equalsIgnoreCase("ELECTRONICS")) {
            return new Electronics("Default Electronics Name"); // Assuming Electronics has a no-argument constructor
        } else if (type.equalsIgnoreCase("GADGET")) {
            return new Gadget("Default Gadget Name"); // Provide a default name or modify as required
        }
        return null;
    }
}

