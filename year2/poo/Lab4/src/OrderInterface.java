package src;

public interface OrderInterface extends IDIdentifiable{
    void addProducts(ProductInterface product, int amount);

    void printOrderStats();

    double getOrderRevenue();
}
