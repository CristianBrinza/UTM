package model;

public interface ClientInterface extends IDIdentifiable {
    void addOrder(int bookId);

    boolean hasOrder(int id);

    boolean isRobber();
}
