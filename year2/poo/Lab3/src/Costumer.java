package Lab3.src;

public class Costumer extends Root {
    protected String name;

    public Costumer(String name) {
        this.name = name;
        this.id = generateId();
    }

    public static void print() {
        System.out.println("A");
    }

    public String getName() {
        return this.name;
    }
}
