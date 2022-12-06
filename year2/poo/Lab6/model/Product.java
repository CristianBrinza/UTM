package model;

public class Product extends Root implements ProductInterface {

    private final double price;
    private final double productExpenses;
    private final int stockSupplyQuantity;
    private boolean orderNeeded = false;

    public Product(double price, double productExpenses, int stockSupplyQuantity) {
        this.id = generateId();
        this.price = price;
        this.productExpenses = productExpenses;
        this.stockSupplyQuantity = stockSupplyQuantity;
        objectsCount += 1;
    }

    public Product(double price, double productExpenses, int stockSupplyQuantity, boolean orderNeeded) {
        this.id = generateId();
        this.price = price;
        this.productExpenses = productExpenses;
        this.stockSupplyQuantity = stockSupplyQuantity;
        this.orderNeeded = orderNeeded;
        objectsCount += 1;
    }

    @Override
    public int getId() {
        return this.id;
    }

    @Override
    public double getPrice() {
        return this.price;
    }

    @Override
    public double getExpenses() {
        return this.productExpenses;
    }

    @Override
    public int getSupplyStockQuantity() {
        return this.stockSupplyQuantity;
    }


    @Override
    public boolean getOrderNeeded() {
        return this.orderNeeded;
    }

}
