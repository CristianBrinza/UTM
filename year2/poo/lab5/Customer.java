import java.util.ArrayList;

public final class Customer extends Root implements CostumerInterface {

    private static int RobberProbability = 1;

    private final ArrayList<Integer> books = new ArrayList<Integer> ( );
    private boolean isRobber = false;

    public Customer ( ) {
        this.id = generateId ( );
        objectsCount += 1;
        if ((int) (Math.random ( ) * 100) > (99 - RobberProbability)) {
            this.isRobber = true;
        }
    }

    public static void setRobberProbability ( int probability ) {
        RobberProbability = probability;
    }

    @Override
    public boolean hasBook ( int id ) {
        return books.contains (id);
    }

    @Override
    public void addBook ( int drugId ) {
        books.add (drugId);
    }

    @Override
    public boolean isRobber ( ) {
        return this.isRobber;
    }

    @Override
    public int getId ( ) {
        return this.id;
    }

}
