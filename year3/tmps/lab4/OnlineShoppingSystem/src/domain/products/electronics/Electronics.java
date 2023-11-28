package domain.products.electronics;


import domain.products.Product;

public class Electronics implements Product {
    private String name;

    public Electronics(String name) {
        this.name = name;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public void describeProduct() {
        System.out.println("This is an electronic item named " + name + ".");
    }

    @Override
    public Product cloneProduct() {
        return null;
    }
}

