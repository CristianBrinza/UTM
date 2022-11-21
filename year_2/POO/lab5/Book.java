public class Book extends Root implements BookInterface {

    private final double price;
    private final double productExpenses;
    private int stockSupplyQuantity;
    private boolean prescriptionNeeded = false;

    public Book ( double price , double productExpenses , int stockSupplyQuantity ) {
        this.id = generateId ( );
        this.price = price;
        this.productExpenses = productExpenses;
        this.stockSupplyQuantity = stockSupplyQuantity;
        objectsCount += 1;
    }

    public Book ( double price , double productExpenses , int stockSupplyQuantity , boolean prescriptionNeeded ) {
        this.id = generateId ( );
        this.price = price;
        this.productExpenses = productExpenses;
        this.stockSupplyQuantity = stockSupplyQuantity;
        this.prescriptionNeeded = prescriptionNeeded;
        objectsCount += 1;
    }

    @Override
    public int getId ( ) {
        return this.id;
    }

    @Override
    public double getPrice ( ) {
        return this.price;
    }

    @Override
    public double getExpenses ( ) {
        return this.productExpenses;
    }

    @Override
    public int getSupplyStockQuantity ( ) {
        return this.stockSupplyQuantity;
    }

    public void setSupplyStockQuantity ( int quantity ) {
        this.stockSupplyQuantity = quantity;
    }

    @Override
    public boolean getPrescriptionNeeded ( ) {
        return this.prescriptionNeeded;
    }

}
