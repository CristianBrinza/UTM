// Import necessary packages and classes for the Main class functionality
// The "domain.models" package contains the primary models like Book, Author, and Genre
import domain.models.*;
// The "domain.patterns.bridge" package contains classes related to the Bridge pattern
// which decouples an abstraction from its implementation, allowing both to vary independently
import domain.patterns.bridge.*;
// The "domain.patterns.builder" package has the BookBuilder class used for the Builder pattern
// which allows constructing complex objects step by step
import domain.patterns.builder.BookBuilder;
// The "domain.patterns.composite" package contains classes for the Composite pattern
// which lets clients treat individual objects and compositions of objects uniformly
import domain.patterns.composite.*;
// The "domain.patterns.decorator" package has classes for the Decorator pattern
// which lets you attach new behaviors to objects by placing them inside special wrapper objects
import domain.patterns.decorator.*;
// The "domain.patterns.facade" package contains the facade class to simplify interfaces
import domain.patterns.facade.BookProductionFacade;
// The "domain.patterns.flyweight" package includes the Flyweight pattern's classes
// which lets you fit more objects into the available amount of RAM by sharing common parts
import domain.patterns.flyweight.AttributeFactory;
// The "domain.patterns.proxy" package contains classes for the Proxy pattern
// which lets you provide a substitute or placeholder for another object
import domain.patterns.proxy.*;

// The Main class serves as the entry point for demonstrating the various design patterns
public class Main {
    // The main method is the starting point of execution for Java applications
    public static void main(String[] args) {
        // === BUILDER PATTERN ===
        // Initialize a BookBuilder object to construct a Book object in steps
        // The builder pattern provides clear separation and a unique layer 
        // for the construction test of a test or other complex objects.
        BookBuilder builder = new BookBuilder();
        // Using the builder to set attributes and finally build the Book object
        Book sampleBook = builder.setTitle("Sample Book")
                .setAuthor(new Author("John Doe", "USA"))
                .setGenre(Genre.FICTION)
                .setISBN("12345")
                .setPrice(20.0)
                .build();
        // Print out the created book's title
        System.out.println("Built Book using Builder Pattern: " + sampleBook.getTitle());

        // === BRIDGE PATTERN ===
        // The Bridge pattern is about preferring composition over inheritance.
        // Here we're separating the abstraction (Book) from its implementation (PrintTechnique)
        PrintTechnique digitalPrint = new DigitalPrint();  // DigitalPrint is one of the implementations
        // Printing the book using its default print technique
        sampleBook.printBook();
        // Update the sampleBook's print technique to DigitalPrint
        // This showcases how we can switch implementations (print techniques) at runtime
        sampleBook = new Book(sampleBook.getTitle(), sampleBook.getAuthor().toString(), sampleBook.getGenre().toString(),
                sampleBook.getISBN(), sampleBook.getPrice(), digitalPrint, new AttributeFactory());
        sampleBook.printBook();  // Printing now uses the DigitalPrint technique

        // === COMPOSITE PATTERN ===
        // The Composite pattern is used to treat individual objects and compositions 
        // of objects uniformly. It creates a tree structure of simple and composite objects
        BookComponent book1 = new SingleBook(sampleBook);
        // Creating another book to add to our collection
        BookComponent book2 = new SingleBook(new Book("Another Book", new Author("Alice", "Unknown").getName(),
                Genre.MYSTERY.toString(), "67890", 15.0, new Lithography(),
                new AttributeFactory()));
        // Creating a book collection to hold multiple books (composite object)
        BookCollection collection = new BookCollection("Sample Collection");
        // Adding individual books to the collection
        collection.addComponent(book1);
        collection.addComponent(book2);
        // Print details of all books in the collection
        collection.printDetails();

        // === DECORATOR PATTERN ===
        // The Decorator pattern allows behaviors to be added to individual objects, 
        // either statically or dynamically, without affecting the behavior of other objects
        // Enhancing the book1 object with a hardcover and signature using decorators
        BookComponent decoratedBook = new HardcoverDecorator(new SignatureDecorator(book1));
        decoratedBook.printDetails();  // Prints the details of the decorated book

        // === FACADE PATTERN ===
        // The Facade pattern provides a simplified interface to a complex subsystem.
        // Here, the BookProductionFacade simplifies the book production and inventory process
        BookProductionFacade facade = new BookProductionFacade();
        // Produce books and add them to the inventory using the facade
        facade.produceAndAddBooksToInventory("Facade Book", new Author("Jane", "UK"), Genre.DRAMA,
                "11223", 25.0, new ScreenPrint(), 100);

        // === FLYWEIGHT PATTERN ===
        // The Flyweight pattern reduces the number of objects created by sharing objects
        // Here, the AttributeFactory helps in creating books with shared attributes
        AttributeFactory attributeFactory = new AttributeFactory();
        // Create a book using the flyweight pattern to share attributes and save memory
        Book flyweightBook = new Book("Flyweight Book", "John Doe", "Fiction", "44556", 20.0, new DigitalPrint(), attributeFactory);
        System.out.println("Created book using Flyweight Pattern: " + flyweightBook.getTitle());

        // === PROXY PATTERN ===
        // The Proxy pattern provides a placeholder for another object to control access to it.
        // Here, the DigitalBookProxy controls access to a RealDigitalBook based on licensing
        DigitalBook realBook = new RealDigitalBook("Proxy Pattern in Java");
        // Create a proxy for the book with a license to read
        DigitalBook proxyWithLicense = new DigitalBookProxy("Proxy Pattern in Java", true);
        // Create another proxy for the book without a license to read
        DigitalBook proxyWithoutLicense = new DigitalBookProxy("Proxy Pattern in Java", false);
        proxyWithLicense.read();  // This proxy has a license, so reading is allowed
        proxyWithoutLicense.read();  // This proxy doesn't have a license, so reading is not allowed
    }
}