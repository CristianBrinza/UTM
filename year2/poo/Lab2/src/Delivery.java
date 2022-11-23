package Lab2.src;

public class Delivery {
    public static int NumberOfCars = 0;
    public static int NumberOfDeliveries = 0;

    private int carId;
    private int destinationStoreId;

    private int bookAmount;
    private int bookId;

    public Delivery() {
        this.carId = generateCarId();
        NumberOfCars += 1;
    }

    private int generateCarId() {
        return (int) ((Math.random() * (9999 - 1000)) + 1000);
    }

    public void deliverBook(

            int destinationPharmacyId,
            int bookId,
            int bookAmount) {
        this.destinationStoreId = destinationStoreId;
        this.bookAmount = bookAmount;
        this.bookId = bookId;
        NumberOfDeliveries += 1;
        System.out.println("Car with id " + this.carId + " delivered an amount of " + this.bookAmount
                + " books with id " + this.bookId + " to the Library with id " + this.destinationStoreId);
    }

    public static void printStats() {
        System.out.println("Total number of cars: " + NumberOfCars);
        System.out.println("Total number of books: " + NumberOfDeliveries);
    }

    public int getCarId() {
        return this.carId;
    }

    public void deliverProduct(int i, int i1, int i2) {
        System.out.println("Delivered");
    }
}
