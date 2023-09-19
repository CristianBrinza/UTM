package factory;

// ISP: Introducing an interface for Factory.


public interface AbstractFactory<T> {
    T create(Object... args);
}
