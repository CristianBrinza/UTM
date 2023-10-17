package client;

import domain.PublicationService;
import domain.BookServiceImpl;
import domain.MagazineServiceImpl;
import factory.PublicationFactory;
import models.Publication;
import java.util.List;



//Single Responsibility Principle (SRP): The Main class is designed to demonstrate the functionality
// of the application. It does not mix other concerns.

//Open/Closed Principle (OCP): The Main class uses the PublicationService interface for both BookServiceImpl
// and MagazineServiceImpl, highlighting the extensibility of the system. If a new type of publication is added in the future, Main doesn't need to change.

//Liskov Substitution Principle (LSP): The Main class can utilize BookServiceImpl and MagazineServiceImpl
// interchangeably through the PublicationService interface. This proves that these implementations can replace the interface without causing issues.

//Interface Segregation Principle (ISP): The Main class only interacts with the necessary methods of
// PublicationService without being burdened by other potential methods that aren't relevant.

//Dependency Inversion Principle (DIP): The Main class depends on the abstraction (PublicationService)
// and not the concrete implementations (BookServiceImpl and MagazineServiceImpl). This means it's more adaptable to changes.

// The Main class serves as the entry point for the application and showcases its functionality.
public class Main {

    // The main method demonstrates how the application can handle both books and magazines.
    public static void main(String[] args) {
        // DIP: Depending on abstraction (PublicationService) rather than concrete classes.
        PublicationService bookService = new BookServiceImpl();
        PublicationService magazineService = new MagazineServiceImpl();

        // Using the factory to create instances of publications.
        Publication book = PublicationFactory.createBook("1984", "George Orwell", "978-0451524935");
        Publication magazine = PublicationFactory.createMagazine("2009", "Time Inc.", "0032-7830");

        // OCP: Using the PublicationService interface allows for extending the system with more types
        // of publications without changing this code.
        bookService.addPublication(book);
        magazineService.addPublication(magazine);

        // LSP: We can use the listPublications method, regardless of whether it's a BookService or MagazineService.
        printPublications(bookService.listPublications());
        printPublications(magazineService.listPublications());
    }

    // SRP: This method has a single responsibility - to print a list of publications.
    private static void printPublications(List<Publication> publications) {
        for (Publication publication : publications) {
            System.out.println("Title: " + publication.getTitle() + ", Author: " + publication.getAuthor() + ", ISBN: " + publication.getISBN());
        }
    }
}
