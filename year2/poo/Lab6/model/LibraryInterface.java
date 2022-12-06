package model;

public interface LibraryInterface extends OrderChecker {
    int checkStock(ProductInterface product, int amount);

    void removeStock(ProductInterface product, int amount);

    void addCash(double profit);

    void robCashRegister();

}

