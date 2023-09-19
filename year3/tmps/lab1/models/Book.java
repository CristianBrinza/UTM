package models;

public class Book implements IBook {
    private int id;
    private String title;
    private String author;

    // SRP: Represents a single entity, a book.
    public Book(int id, String title, String author) {
        this.id = id;
        this.title = title;
        this.author = author;
    }

    // Implementations of IBook methods
    @Override
    public int getId() { return id; }
    @Override
    public String getTitle() { return title; }
    @Override
    public String getAuthor() { return author; }
}
