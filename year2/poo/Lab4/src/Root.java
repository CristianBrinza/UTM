package Lab4.src;

public abstract class Root {
    public static int objectsCount;
    protected int id;

    public int generateId() {
        return (int) ((Math.random() * (99999 - 10000)) + 10000);
    }

    public int getId() {
        return this.id;
    }
}
