package patterns.creational.builder;

public class ConcreteProductBuilder implements ProductBuilder {
    private Product product;

    public ConcreteProductBuilder() {
        this.product = new Product();
    }

    @Override
    public void buildPartA() {
        product.setPartA("Part A of Product");
    }

    @Override
    public void buildPartB() {
        product.setPartB("Part B of Product");
    }

    @Override
    public Product getResult() {
        return product;
    }
}
