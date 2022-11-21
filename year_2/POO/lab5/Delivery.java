public class Delivery extends Root implements IDIdentifiable {

    public Delivery ( ) {
        objectsCount += 1;
        this.id = generateId ( );
    }

    public static void printStats ( ) {
        System.out.println ("Total number of cars: " + objectsCount);
    }

    public void deliverProduct ( ) {
    }

    @Override
    public int getId ( ) {
        return this.id;
    }
}
