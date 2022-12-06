package src;

public abstract class Root {
    public static int objectsCount;

    public int id;

    public int generateId() {
        return (int) ((Math.random() * (9999 - 1000)) + 1000);
    }

}
