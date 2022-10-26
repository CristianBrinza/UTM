package Lab3.src;

public final class Security extends Car {

    private int robberId;

    public Security() {
        super();
    }

    public void arrestRobber(int customerId, int pharmacyId) {
        this.robberId = customerId;
        this.destinationPharmacyId = pharmacyId;
        System.out.println("Security with car id " + this.id + " arrested the customer with id " + this.robberId
                + " which tried to rob the pharmacy with id " + this.destinationPharmacyId);
        numberOfActions += 1;
    }

    @Override
    public void printStats() {
        System.out.println("Total number of cars: " + objectsCount);
        System.out.println("Total number of arrests: " + numberOfActions);
    }

    public void arrestRobber(int i) {

        this.destinationPharmacyId = i;
        System.out.println("Security with car id " + this.id + " arrested the customer with id " + this.robberId
                + " which tried to rob the pharmacy with id " + this.destinationPharmacyId);
        numberOfActions += 1;
    }
}
