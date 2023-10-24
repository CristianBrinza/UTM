package domain.models;

import domain.patterns.bridge.PrintTechnique;
import domain.patterns.flyweight.AttributeFactory;

public class Book {
    private String title;
    private Author author;
    private Genre genre;
    private String isbn;
    private double price;
    private int stockQuantity;
    private PrintTechnique printTechnique;  // Reference to the PrintTechnique interface

    // Constructor to initialize a book with printing technique
    public Book(String title, String authorName, String genreName, String isbn, double price,
                PrintTechnique printTechnique, AttributeFactory attributeFactory) {
        this.title = title;
        this.author = attributeFactory.getAuthor(authorName);  // Use AttributeFactory to get Author object
        this.genre = Genre.valueOf(genreName.toUpperCase());    // Convert genre name to Genre enum
        this.isbn = isbn;
        this.price = price;
        this.stockQuantity = 0; // Initial stock is set to zero
        this.printTechnique = printTechnique;
    }

    // Method to increase stock
    public void addStock(int quantity) {
        this.stockQuantity += quantity;
    }

    // Method to execute the printing of the book
    public void printBook() {
        printTechnique.print(title + " by " + author.getName());  // Use the print method of the specified technique
    }

    // Getter methods
    public String getTitle() {
        return title;
    }

    public Author getAuthor() {
        return author;
    }

    public Genre getGenre() {
        return genre;
    }

    public String getISBN() {
        return isbn;
    }

    public double getPrice() {
        return price;
    }
}
