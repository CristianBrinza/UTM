
# TMPS Lab 3 - Design Patterns Project

## Introduction
This project demonstrates the implementation of various design patterns in Java, including their structure, purpose, and real-world application. Each design pattern is well-commented and elaborated upon to provide a clear understanding of its use and benefits.

## Setup and Execution
To run the project:
1. Ensure you have Java installed on your machine.
2. Navigate to the project directory.
3. Compile the Java files.
4. Run the `Main.java` file to see the design patterns in action.

## Structure:

-  lab3 - Root directory
    - client - Contains the client code (Main.java)
    - domain - Contains domain logic, further divided into:
        - models - Contains domain models
            - Author
            - Book
            - Genre
            - Order
        - patterns - Contains implementations of various design patterns:
            - adapter - Adapter pattern implementation (ThirdPartyPrinter, PrinterAdapter)
            - bridge - Bridge pattern implementation (PrintTechnique, DigitalPrint, ScreenPrint, Lithography)
            - builder - Builder pattern implementation (BookBuilder)
            - composite - Composite pattern implementation (BookComponent, SingleBook, BookCollection)
            - decorator - Decorator pattern implementation (BookDecorator, BonusContentDecorator, SignatureDecorator, HardcoverDecorator)
            - facade - Facade pattern implementation (BookProductionFacade)
            - flyweight - Flyweight pattern implementation (AttributeFactory)
            - proxy - Proxy pattern implementation (DigitalBook, RealDigitalBook, DigitalBookProxy)


### Main.java client code:

- Builder Pattern: A BookBuilder is used to build a sample book.
- Bridge Pattern: The sampleBook is printed, and then a new DigitalPrint technique is applied to it.
- Composite Pattern: Two books are created, and both are added to a BookCollection. The collection details are then printed.
- Decorator Pattern: The first book (book1) is decorated with a SignatureDecorator and a  HardcoverDecorator, after which its details are printed.
- Facade Pattern: The BookProductionFacade is used to produce books and add them to inventory.
- Flyweight Pattern: A Book is created using the AttributeFactory to demonstrate the Flyweight pattern.
- Proxy Pattern: A digital book (RealDigitalBook) is created. Two proxies for the digital book are also created, one with a license and one without. Both proxies are then read.

## Design Patterns Implemented

### Builder Pattern
The Builder Pattern provides clear separation and a unique layer for constructing complex objects step by step. It allows constructing different representations of the same type of object.

**Implementation in the Project:**
The `BookBuilder` class in the `builder` package facilitates the step-by-step construction of a `Book` object.
```java
BookBuilder builder = new BookBuilder();
Book sampleBook = builder.setTitle("Sample Book")
                .setAuthor(new Author("John Doe", "USA"))
                .setGenre(Genre.FICTION)
                .setISBN("12345")
                .setPrice(20.0)
                .build();
```

### Bridge Pattern
The Bridge Pattern decouples an abstraction from its implementation, allowing both to vary independently. It promotes composition over inheritance.

**Implementation in the Project:**
The `PrintTechnique` interface provides multiple print techniques, such as `DigitalPrint` and `Lithography`. The `Book` class can switch its print technique at runtime without altering its structure.
```java
PrintTechnique digitalPrint = new DigitalPrint();
sampleBook = new Book(sampleBook.getTitle(), sampleBook.getAuthor().toString(), sampleBook.getGenre().toString(),
                sampleBook.getISBN(), sampleBook.getPrice(), digitalPrint, new AttributeFactory());
```

### Composite Pattern
The Composite Pattern lets clients treat individual objects and compositions of objects uniformly. It creates a tree structure.

**Implementation in the Project:**
The `BookComponent` interface allows treating both `SingleBook` and `BookCollection` uniformly. Books can be added to a collection, and their details can be printed collectively.
```java
BookComponent book1 = new SingleBook(sampleBook);
BookCollection collection = new BookCollection("Sample Collection");
collection.addComponent(book1);
collection.printDetails();
```

... [More patterns and their implementations]

## Conclusion
This project serves as a comprehensive guide to understanding and implementing various design patterns in Java. Each pattern is thoroughly explained with its purpose, structure, and real-world application in the project. This can serve as a foundation for building robust, scalable, and maintainable software applications.

## Proxy Pattern

The **Proxy Pattern** provides a placeholder for another object to control access to it.

### Implementation in the project:
The project uses the Proxy Pattern to control access to a digital book based on licensing.
```java
DigitalBook realBook = new RealDigitalBook("Proxy Pattern in Java");
DigitalBook proxyWithLicense = new DigitalBookProxy("Proxy Pattern in Java", true);
DigitalBook proxyWithoutLicense = new DigitalBookProxy("Proxy Pattern in Java", false);
proxyWithLicense.read();
proxyWithoutLicense.read();
```
Here, `DigitalBookProxy` controls access to a `RealDigitalBook`. Depending on whether a license is provided, reading the book is either allowed or denied.

---

## Adapter Pattern

The **Adapter Pattern** allows classes with incompatible interfaces to work together. It acts as a bridge between two incompatible interfaces.

### Implementation in the project:
The project implements the Adapter Pattern to provide compatibility between our system and a third-party printer service.
```java
ThirdPartyPrinter thirdPartyPrinter = new ThirdPartyPrinter();
PrinterAdapter printerAdapter = new PrinterAdapter(thirdPartyPrinter);
printerAdapter.requestPrint("Sample Content");
```
In this implementation, the `PrinterAdapter` class bridges the gap between our system's printing method and the third-party printer's method.

---

## Conclusion

This project showcases the implementation and usage of various structural design patterns in Java. Each pattern is demonstrated with practical examples in the context of a book management system. The patterns provide solutions to common design challenges, allowing for more maintainable, scalable, and organized code.

By understanding and implementing these patterns, developers can ensure that they are adhering to best practices, leading to cleaner and more efficient codebases.


