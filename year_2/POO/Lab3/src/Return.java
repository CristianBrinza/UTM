package Lab3.src;

public final class Return extends Order {

    public Return() {
        super();
    }

    @Override
    public void addProducts(int productId, float productPrice, float productExpenses, int amount) {
        if (productPrice > 0 && amount > 0 && productExpenses > 0) {
            this.totalRevenue -= productPrice * amount;
            this.totalProfit -= (productPrice - productExpenses) * amount;
            this.itemsAmount += amount;
            System.out.println(amount + " of items with id " + productId + " were returned to the pharmacy.");
        } else
            System.out.println("Not a valid input!");
    }

    @Override
    public void orderStats() {
        System.out.println("Total revenue loss: " + this.totalRevenue);
        System.out.println("Total profit loss: " + this.totalProfit);
        System.out.println("Total number of returned items: " + this.itemsAmount);
    }

    public void returnProducts(int i, float v, float v1, int i1) {
    }
}
