package Lab3.src;

public final class Delivery extends Car {

    private int productId;
    private int productAmount;

    public Delivery() {
        super();
    }

    public void deliverProduct(

            int destinationPharmacyId,
            int productId,
            int productAmount) {
        this.destinationPharmacyId = destinationPharmacyId;
        this.productAmount = productAmount;
        this.productId = productId;
        numberOfActions += 1;
        System.out.println("Car with id " + this.id + " delivered an amount of " + this.productAmount
                + " products with id " + this.productId + " to the pharmacy with id " + this.destinationPharmacyId);
    }

    @Override
    public void printStats() {
        System.out.println("Total number of cars: " + objectsCount);
        System.out.println("Total number of deliveries: " + numberOfActions);
    }
}
