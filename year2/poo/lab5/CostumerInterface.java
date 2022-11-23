public interface CostumerInterface extends IDIdentifiable {
    void addBook ( int bookId );

    boolean hasBook ( int id );

    boolean isRobber ( );
}