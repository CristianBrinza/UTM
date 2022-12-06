package src;

public interface LibraryInterface extends OrderChecker {
    int checkStock(ProductInterface product, int amount);

    void removeStock(ProductInterface product, int amount);

    public void addCash(double profit);

    public void robCashRegister();

}
