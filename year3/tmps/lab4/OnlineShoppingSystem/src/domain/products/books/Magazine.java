package domain.products.books;


import domain.Product;

public class Magazine implements Product {
    private String name;

    public Magazine(String name) {
        this.name = name;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public String getDescription() {
        return null;
    }

    @Override
    public double getPrice() {
        return 0;
    }

    @Override
    public void describeProduct() {
        System.out.println("This is a magazine named " + name + ".");
    }

    @Override
    public Product cloneProduct() {
        return null;
    }
}

