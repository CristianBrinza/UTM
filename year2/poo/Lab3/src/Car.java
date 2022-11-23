package Lab3.src;

public abstract class Car extends Root {
    public static int numberOfActions = 0;

    protected int destinationPharmacyId;

    public Car() {
        objectsCount += 1;
        generateId();
    }

    public void printStats() {
        System.out.println("Total number of cars: " + objectsCount);
        System.out.println("Total number of actions: " + numberOfActions);
    }
}
