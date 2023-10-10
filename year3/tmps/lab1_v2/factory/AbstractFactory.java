package factory;

/**
 * The AbstractFactory interface defines a generic method for creating instances.
 * It adheres to the Dependency Inversion Principle (DIP) by allowing high-level
 * modules to depend on its abstraction rather than on low-level modules.
 */
public interface AbstractFactory<T> {
    T create(String type);
}

