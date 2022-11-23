public interface OrderInterface extends IDIdentifiable {
    void addProducts ( BookInterface product , int amount );

    void printOrderStats ( );

    double getOrderProfit ( );

    double getOrderRevenue ( );

}
