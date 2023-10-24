package domain.models;

import java.util.ArrayList;
import java.util.List;

public class Author {
    private String name;
    private String biography;
    private List<Book> booksWritten;

    // Constructor to initialize an author with a name and biography
    public Author(String name, String biography) {
        this.name = name;
        this.biography = biography;
        this.booksWritten = new ArrayList<>();
    }

    // Adds a book to the list of books written by the author
    public void addBook(Book book) {
        booksWritten.add(book);
    }

    // Getters and setters
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getBiography() {
        return biography;
    }

    public void setBiography(String biography) {
        this.biography = biography;
    }

    public List<Book> getBooksWritten() {
        return booksWritten;
    }
}
