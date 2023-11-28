package patterns.creational.builder;

public interface ProductBuilder {
    void buildPartA();
    void buildPartB();
    Product getResult();
}

