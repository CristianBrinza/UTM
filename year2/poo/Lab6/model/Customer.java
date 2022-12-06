package model;

import java.util.ArrayList;
import java.util.Random;

public final class Customer extends Root implements ClientInterface {

    private static int RobberProbability = 1;

    private final ArrayList<Integer> orders = new ArrayList<Integer>();
    private boolean isRobber = false;

    public Customer() {
        this.id = generateId();
        objectsCount += 1;
        Random rand = new Random();
        if (rand.nextInt(100) > (99 - RobberProbability)) {
            this.isRobber = true;
        }
    }

    public static void setRobberProbability(int probability) {
        RobberProbability = probability;
    }

    @Override
    public boolean hasOrder(int id) {
        return orders.contains(id);
    }

    @Override
    public void addOrder(int bookId) {
        orders.add(bookId);
    }

    @Override
    public boolean isRobber() {
        return this.isRobber;
    }

    @Override
    public int getId() {
        return this.id;
    }

}
