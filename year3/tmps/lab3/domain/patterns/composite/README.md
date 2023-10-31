
# Composite Design Pattern

## Introduction
The Composite pattern allows you to compose objects into tree structures to represent part-whole hierarchies. It lets clients treat individual objects and compositions of objects uniformly. The pattern provides a mechanism to treat individual objects and compositions of objects as a single entity.


The Composite pattern allows you to treat individual objects and compositions of objects uniformly. This pattern is especially useful for hierarchical structures.

In this implementation, the Composite pattern is used to represent both individual books (`SingleBook`) and collections of books (`BookCollection`).

## Classes Involved
1. **BookComponent (Interface)**: Represents the component for both individual books and collections. It sets a contract for both the composite (BookCollection) and leaf (SingleBook) objects.
2. **SingleBook (Class)**: Represents individual books and implements the `BookComponent` interface. It is a leaf in the Composite pattern.
3. **BookCollection (Class)**: Represents a collection of books or other collections and implements the `BookComponent` interface. It is a composite object in the Composite pattern.

## How it works
The `BookComponent` interface provides methods that are common to both individual books and collections of books. The `SingleBook` class represents individual books, whereas the `BookCollection` class represents a collection of books or other collections. The `BookCollection` class can contain other `BookComponent` objects, allowing for complex nested structures.

Clients can treat both `SingleBook` and `BookCollection` uniformly, as they both implement the `BookComponent` interface.

## Conclusion
The Composite pattern provides a solution to represent part-whole hierarchies. In our context, it allows representing both individual books and collections of books (or other collections) in a unified manner.



### **Use-Case for Book Factory:**
Consider books and collections of books (e.g., series or sets). 

Both a single book and a collection of books should have common operations, like getting the price or printing details. Using the Composite pattern, we can treat both individual books and collections uniformly.



- **BookComponent interface:** An interface that defines common operations for both individual books and collections.
- **SingleBook class:** Represents individual books and implements the BookComponent interface.
- **BookCollection class:** Represents a collection of books (or other collections) and also implements the BookComponent interface.