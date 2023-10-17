// This is the package declaration. All the classes and interfaces within this directory belong to the 'factory' package.
package factory;




//ingle Responsibility Principle (SRP): The PublicationFactory class has a clear responsibility: to create and
// return instances of different types of publications.

//Liskov Substitution Principle (LSP): The methods return instances that adhere to the Publication contract.
// Thus, the returned instances can be used wherever a Publication is expected.

//Dependency Inversion Principle (DIP): The factory methods return abstract Publication types rather than
// concrete implementations, which ensures that the client code depends on abstractions, not on concrete implementations.









// Import necessary classes and interfaces from the 'models' package.
import models.Book;
import models.Magazine;
import models.Publication;

// The 'PublicationFactory' class declaration.
// This class is responsible for creating instances of different types of publications (i.e., books and magazines).
public class PublicationFactory {

    // Static method to create and return an instance of a 'Book'.
    // This method takes the title, author, and ISBN as parameters.
    public static Publication createBook(String title, String author, String ISBN) {
        return new Book(title, author, ISBN) {
            @Override
            public String getTitle() {
                return null; // This should return the title. It seems there's an oversight here.
            }

            @Override
            public String getType() {
                return null; // This should return the type (e.g., "Book"). Another oversight.
            }
        };
    }

    // Static method to create and return an instance of a 'Magazine'.
    // This method takes the title, author, and ISBN as parameters.
    public static Publication createMagazine(String title, String author, String ISBN) {
        return new Magazine(title, author, ISBN) {
            @Override
            public String getType() {
                return null; // This should return the type (e.g., "Magazine"). Oversight noticed.
            }
        };
    }
}
