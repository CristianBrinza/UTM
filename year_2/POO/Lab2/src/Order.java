package Lab2.src;

public class Order {
    public static int NumberOfOrders;
    public static int Amount;

    private int id;
    private int itemsAmount;
    private float totalRevenue = 0;
    private float totalProfit = 0;

    public Order() {
        NumberOfOrders++;
        this.id = generateOrderId();
    }

    private int generateOrderId() {
        return (int) ((Math.random() * (99999 - 10000)) + 10000);
    }

    // We call this method for every distinct product:
    public void addProducts(int productId, float productPrice, float productExpenses, int amount) {
        if (productPrice > 0 && amount > 0 && productExpenses > 0) {
            this.totalRevenue += productPrice * amount;
            this.totalProfit += (productPrice - productExpenses) * amount;
            Amount += amount;
            System.out.println(amount + " of items with id " + productId + " were added to the order.");
        } else
            System.out.println("Not a valid input!");
    }

    public static void printStats() {
        System.out.println("Total number of orders: " + NumberOfOrders);
        System.out.println("Total number of sold products: " + Amount);
    }

    public void orderStats() {
        System.out.println("Total number of orders: " + NumberOfOrders);
        System.out.println("Total number of sold products: " + Amount);
    }

    public int getId() {
        return this.id;
    }

    public int getOrderId() {
        return this.id;
    }

    public int getItemsAmount() {
        return this.itemsAmount;
    }

    public float getTotalRevenue() {
        return this.totalRevenue;
    }

    public float getTotalProfit() {
        return this.totalProfit;
    }

}
