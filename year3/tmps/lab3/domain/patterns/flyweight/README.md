# Flyweight Design Pattern

## Introduction
The Flyweight pattern is used to reduce the number of objects created, to decrease memory footprint and increase performance. It shares as much memory as possible with similar objects. This pattern provides a way to use objects in large numbers when a simple repeated representation would use an unacceptable amount of memory.

In this implementation, the Flyweight pattern is used to manage shared attributes like genre and author, ensuring that they are not duplicated but are instead shared among different books to save memory.

## Classes Involved
1. **AttributeFactory (Class)**: Factory class to produce and manage shared attributes using the Flyweight pattern. This class has methods to retrieve genres and authors, ensuring that shared attributes are not duplicated.

## How it works
The `AttributeFactory` class provides methods to retrieve genres and authors. If an author doesn't exist in its internal map, a new author is created, stored, and then returned. For genres, the factory directly returns the corresponding enum value.

This approach ensures that shared attributes, like a particular author, exist only once in memory. When a book requires an author, it gets a reference to the shared author object rather than creating a new one.

## Conclusion
The Flyweight pattern is a memory-saving technique that is useful when dealing with a large number of objects that have shared attributes. In our context, it allows efficient management of shared book attributes like genres and authors.


## Flyweight Pattern:
The Flyweight pattern is used to reduce the number of objects created, decrease memory footprint, and increase performance by sharing as much data as possible with similar objects. The pattern is particularly useful when a large number of objects need to be created and they share a lot of information.

### Use-Case for Book Factory:
Consider the case where the book factory needs to produce a large number of books that have shared attributes, such as genre or author. Instead of creating a new instance for each attribute every time a book is produced, the Flyweight pattern can be used to reuse existing instances.



- **AttributeFactory:** This factory will produce shared attributes (like genre or author) and will store them for reuse.
- Update the **Book** class to utilize the AttributeFactory for getting genre and author instances.


```java

public class Book {
    private String title;
    private Author author;
    private Genre genre;
    // ... (rest of the attributes)

    // Constructor now takes an AttributeFactory to get genre and author instances
    public Book(String title, String authorName, String genreName, String isbn, double price, 
                PrintTechnique printTechnique, AttributeFactory attributeFactory) {
        this.title = title;
        this.author = attributeFactory.getAuthor(authorName);
        this.genre = attributeFactory.getGenre(genreName);
        // ... (rest of the initialization)
    }

    // ... (rest of the class)
}
```