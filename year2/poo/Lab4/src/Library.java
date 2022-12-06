package src;

import java.util.HashMap;

public final class Library extends Root implements LibraryInterface {
    public static int totalSales;
    protected HashMap<Integer, Integer> stock = new HashMap<Integer, Integer>();
    private int productID, amount, updatedAmount;
    private int salesOfCurrentDay;

    private OrderChecker librarian;
    private IDIdentifiable deliveryCar;
    private SecurityInterface securityCar;

    public Library() {
        this.id = generateId();
        objectsCount++;
    }

    public void supplyStock(ProductInterface product) {
        this.productID = product.getId();
        this.amount = product.getSupplyStockQuantity();
        if (stock.containsKey(productID)) {
            this.updatedAmount = amount + stock.get(productID);
            stock.replace(productID, updatedAmount);
        } else {
            stock.put(productID, amount);
        }
        System.out.println(" ");
        System.out.println("Car with id " + deliveryCar.getId() + " delivered the product");
        System.out.println(
                "Library with id " + this.id + " supplied an amount of " + amount + " items of id " + productID);
        System.out.println("Now the current stock quantity for this product is " + stock.get(productID));
    }

    @Override
    public int checkStock(ProductInterface product, int amount) {
        productID = product.getId();
        if (!stock.containsKey(productID) || stock.get(productID) == 0) {
            System.out.println("The chosen product is out of stock");
            return 0;
        }
        if (stock.get(productID) < amount) {
            System.out.println("Stock is less than needed amount of " + amount + " items. The library will sell only "
                    + stock.get(productID)
                    + " items of this product");
            return stock.get(productID);
        }
        return amount;
    }

    @Override
    public void removeStock(ProductInterface product, int amount) {
        this.productID = product.getId();
        int updatedAmount = stock.get(productID) - amount;
        stock.replace(productID, updatedAmount);
    }

    @Override
    public void checkOrder(boolean orderPresent) {
        librarian.checkOrder(orderPresent);
    }

    @Override
    public int getId() {
        return this.id;
    }

    public void setLibrarian(OrderChecker currentLibrarian) {
        this.librarian = currentLibrarian;
    }

    public void setDeliveryCar(IDIdentifiable car) {
        this.deliveryCar = car;
    }

    public void setSecurityCar(SecurityInterface car) {
        this.securityCar = car;
    }

    @Override
    public void addCash(double profit) {
        this.salesOfCurrentDay += profit;
        System.out.println(profit + " dollars added to the cash register of the library with id " + this.id);
    }

    // Take all the cash at the end of the day:
    public void resetCashRegister() {
        totalSales += salesOfCurrentDay;
        salesOfCurrentDay = 0;
    }

    @Override
    public void robCashRegister() {
        if (securityCar.arrestRobber()) {
            return;
        } else {
            salesOfCurrentDay = 0;
        }
    }

}
