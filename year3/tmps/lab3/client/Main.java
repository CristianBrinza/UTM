package client;

import domain.models.*;
import domain.patterns.bridge.*;
import domain.patterns.builder.BookBuilder;
import domain.patterns.composite.*;
import domain.patterns.decorator.*;
import domain.patterns.facade.BookProductionFacade;
import domain.patterns.flyweight.AttributeFactory;
import domain.patterns.proxy.*;

public class Main {
    public static void main(String[] args) {
        // Builder Pattern
        BookBuilder builder = new BookBuilder();
        Book sampleBook = builder.setTitle("Sample Book")
                .setAuthor(new Author("John Doe", "USA"))  // Corrected the Author instantiation
                .setGenre(Genre.FICTION)  // Corrected the Genre reference
                .setISBN("12345")
                .setPrice(20.0)
                .build();
        System.out.println("Built Book using Builder Pattern: " + sampleBook.getTitle());

        // Bridge Pattern
        PrintTechnique digitalPrint = new DigitalPrint();
        sampleBook.printBook();
        sampleBook = new Book(sampleBook.getTitle(), sampleBook.getAuthor().toString(), sampleBook.getGenre().toString(),
                sampleBook.getISBN(), sampleBook.getPrice(), digitalPrint, new AttributeFactory());

        sampleBook.printBook();  // This uses the DigitalPrint technique

        // Composite Pattern
        BookComponent book1 = new SingleBook(sampleBook);
        BookComponent book2 = new SingleBook(new Book("Another Book", new Author("Alice", "Unknown").getName(),
                Genre.MYSTERY.toString(), "67890", 15.0, new Lithography(),
                new AttributeFactory()));
        BookCollection collection = new BookCollection("Sample Collection");
        collection.addComponent(book1);
        collection.addComponent(book2);
        collection.printDetails();

        // Decorator Pattern
        BookComponent decoratedBook = new HardcoverDecorator(new SignatureDecorator(book1));
        decoratedBook.printDetails();

        // Facade Pattern
        BookProductionFacade facade = new BookProductionFacade();
        facade.produceAndAddBooksToInventory("Facade Book", new Author("Jane", "UK"), Genre.DRAMA,
                "11223", 25.0, new ScreenPrint(), 100);

        // Flyweight Pattern
        AttributeFactory attributeFactory = new AttributeFactory();
        Book flyweightBook = new Book("Flyweight Book", "John Doe", "Fiction", "44556", 20.0, new DigitalPrint(), attributeFactory);
        System.out.println("Created book using Flyweight Pattern: " + flyweightBook.getTitle());

        // Proxy Pattern
        DigitalBook realBook = new RealDigitalBook("Proxy Pattern in Java");
        DigitalBook proxyWithLicense = new DigitalBookProxy("Proxy Pattern in Java", true);
        DigitalBook proxyWithoutLicense = new DigitalBookProxy("Proxy Pattern in Java", false);
        proxyWithLicense.read();
        proxyWithoutLicense.read();
    }
}
