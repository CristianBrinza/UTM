package model;

public interface ProductInterface extends IDIdentifiable {
    double getPrice();

    double getExpenses();

    int getSupplyStockQuantity();

    boolean getOrderNeeded();

}
