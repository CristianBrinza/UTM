package Lab2.src;

public class Return {
    public static int NumberOfReturns;
    public static int Amount;

    private int id;
    private int itemsAmount;
    private float totalRevenueLoss = 0;
    private float totalProfitLoss = 0;

    public Return() {
        NumberOfReturns++;
        this.id = generateOrderId();
    }

    private int generateOrderId() {
        return (int) ((Math.random() * (99999 - 10000)) + 10000);
    }

    // We call this method for every distinct product:
    public void returnProducts(int productId, float productPrice, float productExpenses, int amount) {
        if (productPrice > 0 && amount > 0 && productExpenses > 0) {
            this.totalRevenueLoss -= productPrice * amount;
            this.totalProfitLoss -= (productPrice - productExpenses) * amount;
            Amount += amount;
            System.out.println(amount + " of items with id " + productId + " were returned to the pharmacy.");
        } else
            System.out.println("Not a valid input!");
    }

    public static void printStats() {
        System.out.println("Total number of returns: " + NumberOfReturns);
        System.out.println("Total number of returned products: " + Amount);
    }

    public void orderStats() {
        System.out.println("Total number of returns: " + NumberOfReturns);
        System.out.println("Total number of returned products: " + Amount);
    }

    public int getId() {
        return this.id;
    }

    public int getReturnId() {
        return this.id;
    }

    public int getItemsAmount() {
        return this.itemsAmount;
    }

    public float getTotalRevenueLoss() {
        return this.totalRevenueLoss;
    }

    public float getTotalProfitLoss() {
        return this.totalProfitLoss;
    }
}
