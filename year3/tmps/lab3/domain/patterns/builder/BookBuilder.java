package domain.patterns.builder;

import domain.models.*;
import domain.patterns.bridge.PrintTechnique;
import domain.patterns.bridge.Lithography;  // Importing Lithography
import domain.patterns.flyweight.AttributeFactory;

// Builder class to construct a Book object
public class BookBuilder {
    private String title;
    private Author author;
    private Genre genre;
    private String isbn;
    private double price;
    private PrintTechnique printTechnique;
    private AttributeFactory attributeFactory;

    public BookBuilder() {
        this.attributeFactory = new AttributeFactory();  // Initialize the AttributeFactory
    }

    public BookBuilder setTitle(String title) {
        this.title = title;
        return this;
    }

    public BookBuilder setAuthor(Author author) {
        this.author = author;
        return this;
    }

    public BookBuilder setGenre(Genre genre) {
        this.genre = genre;
        return this;
    }

    public BookBuilder setISBN(String isbn) {
        this.isbn = isbn;
        return this;
    }

    public BookBuilder setPrice(double price) {
        this.price = price;
        return this;
    }

    public BookBuilder setPrintTechnique(PrintTechnique printTechnique) {
        this.printTechnique = printTechnique;
        return this;
    }

    public Book build() {
        if (printTechnique == null) {
            printTechnique = new Lithography();  // Default print technique
        }
        return new Book(title, author.toString(), genre.toString(), isbn, price, printTechnique, attributeFactory);  // Using toString() to get names
    }
}
