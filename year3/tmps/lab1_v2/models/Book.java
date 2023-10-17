// This is the package declaration. All the classes and interfaces within this directory belong to the 'models' package.
package models;



//Single Responsibility Principle (SRP): The Book class, even though abstract, is centered around the concept
// of a book and its primary attributes. The class has a clear responsibility to provide base properties and behaviors of a book.

//Open/Closed Principle (OCP): As the class is abstract, it inherently invites subclasses to extend and provide
// specific implementations without needing to modify the base behavior in the Book class.

//Liskov Substitution Principle (LSP): The Book class implements the Publication interface. Hence any subclass of
// Book can be substituted in places where Publication is expected.

//Dependency Inversion Principle (DIP): The Book class relies on the abstraction provided by the Publication interface
// rather than concrete implementations.






// The 'Book' class declaration.
// This class is declared as 'abstract', meaning that it cannot be instantiated directly.
// It must be subclassed by other classes. The 'Book' class implements the 'Publication' interface.
public abstract class Book implements Publication {

    // Private instance variable to store the title of the book.
    private String title;

    // Private instance variable to store the author of the book.
    private String author;

    // Private instance variable to store the ISBN (International Standard Book Number) of the book.
    private String ISBN;

    // Constructor for the 'Book' class. It takes the title, author, and ISBN as parameters.
    public Book(String title, String author, String ISBN) {
        // Initialize the 'author' instance variable with the provided value.
        this.author = author;

        // Initialize the 'ISBN' instance variable with the provided value.
        this.ISBN = ISBN;

        // Note: The 'title' parameter isn't used to initialize the 'title' instance variable. This might be an oversight.
    }

    // Implementation of the 'getAuthor()' method from the 'Publication' interface.
    // This method returns the author of the book.
    @Override
    public String getAuthor() {
        return author;
    }

    // Implementation of the 'getISBN()' method from the 'Publication' interface.
    // This method returns the ISBN of the book.
    @Override
    public String getISBN() {
        return ISBN;
    }
}
