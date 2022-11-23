package Lab3.src;

public final class Casier extends Costumer {
    private int StoreId;
    private float totalSales;

    public Casier(String name, int storeId) {
        super(name);
        this.id = generateId();
        this.StoreId = StoreId;
    }

    public static void print() {
        System.out.println("B");
    }

    public void sellbookss(int productId, int customerId, float totalPrice, boolean prescribtionNeeded) {
        if (prescribtionNeeded == true)
            System.out.println("Prescribtion checked");
        System.out.println("Pharmacist sold product with id " + productId + " to the customer with id " + customerId);
        this.totalSales += totalPrice;
    }

    public void setStoreId(int id) {
        this.id = StoreId;
    }

    public int getStoreId() {
        return this.StoreId;
    }

    public float getTotalSales() {
        return this.totalSales;
    }

}
