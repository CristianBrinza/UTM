// This is the package declaration. All the classes and interfaces within this directory belong to the 'models' package.
package models;



//Single Responsibility Principle (SRP): The Magazine class is designed with a singular focus: to represent a magazine.
// It has properties like title, author, and ISBN and methods to retrieve them.

//Liskov Substitution Principle (LSP): The Magazine class implements the Publication interface. This means any subclass of
// Magazine should be able to be used wherever a Publication is expected.

//Interface Segregation Principle (ISP): The Magazine class only implements methods that are relevant to it
// from the Publication interface.








// The 'Magazine' class declaration.
// This class is declared as 'abstract', meaning that it cannot be instantiated directly.
// It must be subclassed by other classes. The 'Magazine' class implements the 'Publication' interface.
public abstract class Magazine implements Publication {

    // Private instance variable to store the title of the magazine.
    private String title;

    // Private instance variable to store the author of the magazine.
    private String author;

    // Private instance variable to store the ISBN (International Standard Book Number) of the magazine.
    private String ISBN;

    // Constructor for the 'Magazine' class. It takes the title, author, and ISBN as parameters.
    public Magazine(String title, String author, String ISBN) {
        // Initialize the 'title' instance variable with the provided value.
        this.title = title;

        // Initialize the 'author' instance variable with the provided value.
        this.author = author;

        // Initialize the 'ISBN' instance variable with the provided value.
        this.ISBN = ISBN;
    }

    // Implementation of the 'getTitle()' method from the 'Publication' interface.
    // This method returns the title of the magazine.
    public String getTitle() { return title; }

    // Implementation of the 'getAuthor()' method from the 'Publication' interface.
    // This method returns the author of the magazine.
    public String getAuthor() { return author; }

    // Implementation of the 'getISBN()' method from the 'Publication' interface.
    // This method returns the ISBN of the magazine.
    public String getISBN() { return ISBN; }
}
