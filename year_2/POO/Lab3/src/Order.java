package Lab3.src;

public class Order extends Root {

    protected int itemsAmount;
    protected float totalRevenue = 0;
    protected float totalProfit = 0;

    public Order() {
        objectsCount++;
        this.id = generateId();
    }

    // We call this method for every distinct product:
    public void addProducts(int productId, float productPrice, float productExpenses, int amount) {
        if (productPrice > 0 && amount > 0 && productExpenses > 0) {
            this.totalRevenue += productPrice * amount;
            this.totalProfit += (productPrice - productExpenses) * amount;
            this.itemsAmount += amount;
            System.out.println(amount + " of items with id " + productId + " were added to the order.");
        } else
            System.out.println("Not a valid input!");
    }

    public static void printStats() {
        System.out.println("Total number of orders: " + objectsCount);
    }

    public void orderStats() {
        System.out.println("Total revenue: " + this.totalRevenue);
        System.out.println("Total profit: " + this.totalProfit);
        System.out.println("Total number of items in order: " + this.itemsAmount);
    }

    public int getOrderId() {
        return this.id;
    }

    public float getTotalRevenue() {
        return this.totalRevenue;
    }

    public float getTotalProfit() {
        return this.totalProfit;
    }

}
