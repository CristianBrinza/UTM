package src;

// One delivery car can be assigned to more libraries
public final class SupplementDelivery extends Root implements IDIdentifiable {

    public SupplementDelivery() {
        objectsCount += 1;
        this.id = generateId();
    }

    public void deliverProduct() {
    }

    public static void printStats() {
        System.out.println("Total number of cars: " + objectsCount);
    }

    @Override
    public int getId() {
        return this.id;
    }

}
