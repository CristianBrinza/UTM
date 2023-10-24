package domain.patterns.facade;

import domain.models.Author;
import domain.models.Book;
import domain.models.Genre;
import domain.patterns.bridge.PrintTechnique;
import domain.patterns.flyweight.AttributeFactory;
import domain.patterns.composite.BookComponent;
import java.util.List;

// Facade class that provides a simplified interface to the complex book production subsystem
public class BookProductionFacade {
    // This is a simplified representation. In a real-world scenario,
    // we would have references to subsystems like BookProduction, Printing, InventoryManagement, etc.

    // Produces a batch of books and adds them to inventory
    public void produceAndAddBooksToInventory(String title, Author author, Genre genre,
                                              String isbn, double price, PrintTechnique printTechnique,
                                              int quantity) {
        // Create an instance of AttributeFactory
        AttributeFactory attributeFactory = new AttributeFactory();

        // 1. Produce the book
        Book book = new Book(title, author.toString(), genre.toString(), isbn, price, printTechnique, attributeFactory);

        // 2. Print the book using the specified technique
        book.printBook();

        // 3. Add the book to inventory (simplified for this demonstration)
        for (int i = 0; i < quantity; i++) {
            // In a real-world application, this line would interact with an InventoryManagement system.
            System.out.println("Added book to inventory: " + title);
        }
    }
}
