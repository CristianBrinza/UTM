package domain.patterns.facade;

import domain.models.Author;
import domain.models.Book;
import domain.models.Genre;
import domain.patterns.bridge.PrintTechnique;
import domain.patterns.flyweight.AttributeFactory;

/**
 * Facade class that provides a simplified interface to the complex book production subsystem.
 * This class encapsulates the complexities involved in producing a book, printing it, 
 * and adding it to the inventory.
 */
public class BookProductionFacade {
    /**
     * Produces a batch of books and adds them to the inventory.
     * 
     * @param title Title of the book.
     * @param author Author of the book.
     * @param genre Genre of the book.
     * @param isbn ISBN of the book.
     * @param price Price of the book.
     * @param printTechnique The printing technique to be used.
     * @param quantity Quantity of books to be produced.
     */
    public void produceAndAddBooksToInventory(String title, Author author, Genre genre,
                                              String isbn, double price, PrintTechnique printTechnique,
                                              int quantity) {
        // Create an instance of AttributeFactory for book attributes
        AttributeFactory attributeFactory = new AttributeFactory();

        // Produce the book with the given attributes
        Book book = new Book(title, author.toString(), genre.toString(), isbn, price, printTechnique, attributeFactory);

        // Print the book using the specified technique
        book.printBook();

        // Add the produced books to inventory (simplified for this demonstration)
        for (int i = 0; i < quantity; i++) {
            // In a real-world application, this line would interact with an InventoryManagement system.
            System.out.println("Added book to inventory: " + title);
        }
    }
}