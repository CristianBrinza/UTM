# Book Publishing Management System

## Project Description

The "Book Publishing Management System" is a Java-based application that demonstrates the implementation and usage of various creational design patterns in a software project. The domain of the project revolves around book publishing, involving entities like books, authors, and publishing houses. The project aims to manage the creation and display of book details, author details, and publishing house collections in a simplified manner.

## Domain: Book Publishing

### Classes/Models/Entities:
- Book (interface)
- EBook and PrintBook (concrete classes)
- BookFactory (factory class)
- Author (prototype class)
- PublishingHouse (builder class)
- PublishingManager (singleton class)


### In this implementation:

- Book Interface: Defines the contract for book classes.
- EBook and PrintBook: Implement the Book interface.
- BookFactory: Implements the Factory Method pattern to create book objects.
- AuthorPrototype: Implements the Prototype pattern to clone author objects.
- PublishingHouse: Implements the Builder pattern to create a publishing house object.
- PublishingManager: Implements the Singleton pattern to manage book creation.


This code demonstrates the usage of the Factory Method, Prototype, Builder, and Singleton design patterns in a cohesive manner within a book publishing domain. 


- Book Interface: Defines the contract for all book classes.
- EBook and PrintBook: Implement the Book interface.
- BookFactory: Implements the Factory Method pattern.
- AuthorPrototype: Implements the Prototype pattern.
- PublishingHouse: Implements the Builder pattern.
- PublishingManager: Implements the Singleton pattern.




## Design Patterns Implemented
1. - Factory Method Pattern
   - Class: BookFactory
   - Purpose: To create objects (books) without specifying the exact class to instantiate.
   - Explanation: The BookFactory class provides a method createBook() that creates and returns objects of EBook or PrintBook based on the input type provided. This abstracts the object creation logic from the client code, promoting code decoupling and scalability.
2. - Prototype Pattern
   - Class: AuthorPrototype and FictionAuthor
   - Purpose: To create new objects by copying an existing object.
   - Explanation: The AuthorPrototype class provides a method clone() that allows creating a new Author object by copying an existing one. The FictionAuthor class extends AuthorPrototype and implements the clone() method, providing a mechanism to duplicate FictionAuthor objects without going through a costly creation process.
3. - Builder Pattern
   - Class: PublishingHouse and its nested Builder class
   - Purpose: To construct a complex object step by step.
   - Explanation: The Builder class inside PublishingHouse provides a mechanism to create a PublishingHouse object by setting its attributes step by step, and then calling the build() method. This pattern is particularly useful when an object needs to be created with many optional components or configurations.
4. - Singleton Pattern
   - Class: PublishingManager
   - Purpose: To restrict the instantiation of a class to a single instance and provide a global point of access to it.
   - Explanation: PublishingManager ensures that a single instance is created and provides a static method getInstance() to access the instance. It manages the creation of books using BookFactory, ensuring that the object creation logic is centralized and managed.





## Example Usage
Creating Books

```java
// Get the single instance of the publishing manager.
PublishingManager publishingManager = PublishingManager.getInstance();

// Create books using the publishing manager.
Book eBook = publishingManager.createBook("EBook", "Digital World", "Alice");
Book printBook = publishingManager.createBook("PrintBook", "Paper Trails", "Bob");
```

Cloning Authors

```java
// Clone an author using the Prototype pattern.
AuthorPrototype author = new FictionAuthor("Author Carol");
AuthorPrototype newAuthor = author.clone();
```
Building a Publishing House
```java
// Build a publishing house using the Builder pattern.
PublishingHouse publishingHouse = new PublishingHouse.Builder()
.setEBook(eBook)
.setPrintBook(printBook)
.build();

// Display information about the books in the publishing house.
publishingHouse.displayBooks();
```

## Conclusion
The "Book Publishing Management System" project provides a practical implementation of various creational design patterns, demonstrating their utility in managing object creation in a flexible and efficient manner. This project can be extended or modified to incorporate more entities, attributes, and functionalities as per specific use-cases and requirements.