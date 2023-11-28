package patterns.creational.builder;

// Builder Interface: Defines the step-by-step construction process for a complex product.
// Builder Interface: Defines the construction process for a Computer.
public interface ComputerBuilder {
    void buildProcessor();
    void buildRAM();
    void buildStorage();
    Computer getResult();
}

