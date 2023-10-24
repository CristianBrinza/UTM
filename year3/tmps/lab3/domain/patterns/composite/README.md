## Composite Pattern:

The Composite pattern allows you to treat individual objects and compositions of objects uniformly. This pattern is especially useful for hierarchical structures.

### **Use-Case for Book Factory:**
Consider books and collections of books (e.g., series or sets). 

Both a single book and a collection of books should have common operations, like getting the price or printing details. Using the Composite pattern, we can treat both individual books and collections uniformly.



- **BookComponent interface:** An interface that defines common operations for both individual books and collections.
- **SingleBook class:** Represents individual books and implements the BookComponent interface.
- **BookCollection class:** Represents a collection of books (or other collections) and also implements the BookComponent interface.