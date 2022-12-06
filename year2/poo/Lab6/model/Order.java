package model;

import java.util.HashMap;

public class Order extends Root implements OrderInterface {

    protected int itemsAmount;
    protected double totalRevenue = 0;
    protected double totalProfit = 0;

    protected HashMap<Integer, Integer> products = new HashMap<Integer, Integer>();

    public Order() {
        objectsCount++;
        this.id = generateId();
    }

    @Override
    public void addProducts(ProductInterface product, int amount) {
        this.totalRevenue += product.getPrice() * amount;
        this.totalProfit += (product.getPrice() - product.getExpenses()) * amount;
        this.itemsAmount += amount;
        products.put(product.getId(), amount);
        System.out.println(amount + " of items with id " + product.getId() + " were added to the order");
    }

    @Override
    public void printOrderStats() {
        System.out.println("Total price for the order: " + this.totalRevenue + " lei");
        System.out.println("Total profit of library from this order: " + this.totalProfit + " lei");
        System.out.println("Total number of items in order: " + this.itemsAmount);
        System.out.println("The list of items ordered (their id and amount): " + this.products);
    }

    @Override
    public double getOrderRevenue() {
        return this.totalRevenue;
    }

    @Override
    public double getOrderProfit() {
        return this.totalProfit;
    }

    @Override
    public int getId() {
        return this.id;
    }

}
