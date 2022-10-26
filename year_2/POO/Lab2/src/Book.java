package Lab2.src;

public class Book {
    public static int NumberOfProducts;

    private int id;
    private String writer;
    private int writerID;
    private float price;
    private float productExpenses;
    private int stock;
    private boolean inStock = true;
    private int stockSupplyQuantity;
    private boolean prescriptionNeeded = false;

    public Book(
            String writer,
            int writerID,
            float price,
            float productExpenses,
            int stockSupplyQuantity) {
        this.id = generateProductId();
        this.writer = writer;
        this.writerID = writerID;
        this.stock = stockSupplyQuantity;
        this.stockSupplyQuantity = stockSupplyQuantity;
        this.price = price;
        this.productExpenses = productExpenses;
        NumberOfProducts += 1;
    }

    public Book(
            String writer,
            int WriterId,
            float price,
            float productExpenses,
            int stockSupplyQuantity,
            boolean prescriptionNeeded) {
        this.id = generateProductId();
        this.writer = writer;
        this.writerID = writerID;
        this.price = price;
        this.productExpenses = productExpenses;
        this.stock = stockSupplyQuantity;
        this.stockSupplyQuantity = stockSupplyQuantity;
        this.prescriptionNeeded = prescriptionNeeded;
    }

    private int generateProductId() {
        return (int) ((Math.random() * (99999 - 10000)) + 10000);
    }

    public void sell(int amount) {
        if (this.stock - amount >= 0) {
            this.stock -= amount;
            System.out.println(amount + " pieces of product were sold. " + this.stock + " items left");
            if (this.stock == 0) {
                this.inStock = false;
                System.out.println("Product out of stock");
            }
        } else {
            supplyStock();
        }
    }

    private void supplyStock() {
        this.stock += stockSupplyQuantity;
        this.inStock = true;
        System.out.println("Product with id " + getId() + " was supplied with " + this.stockSupplyQuantity + " items");
    }

    public String getWriter() {
        return this.writer;
    }

    public int getWriterId() {
        return this.writerID;
    }

    public int getId() {
        return this.id;
    }

    public float getPrice() {
        return this.price;
    }

    public float getProductExpenses() {
        return this.productExpenses;
    }

    public boolean getPrescriptionNeeded() {
        return this.prescriptionNeeded;
    }

    public boolean isInStock() {
        return inStock;
    }
}
