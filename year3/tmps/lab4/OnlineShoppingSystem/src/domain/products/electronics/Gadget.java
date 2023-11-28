package domain.products.electronics;

import domain.products.Product;

public class Gadget implements Product {
    private String name;

    public Gadget(String name) {
        this.name = name;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public void describeProduct() {
        System.out.println("This is a gadget named " + name + ".");
    }

    @Override
    public Product cloneProduct() {
        return null;
    }
}
