package models;

/**
 * IProduct interface defines the contract for Product entities.
 * It adheres to the Interface Segregation Principle (ISP) by providing a clear
 * and relevant set of functionalities (getName and getPrice) to the implementing class.
 */
public interface IProduct {
    String getName();
    double getPrice();
}
