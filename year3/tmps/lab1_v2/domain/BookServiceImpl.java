// This package 'domain' focuses on the business operations linked to publications.
package domain;



//Single Responsibility Principle (SRP): BookServiceImpl has one clear responsibility: to manage operations related
// to books. It maintains a list of books and provides methods to add to and list those books.

//Open/Closed Principle (OCP): BookServiceImpl is an implementation of the PublicationService interface. If there's a
// need to introduce new functionalities specific to books in the future, we can do so in this class without modifying the interface.

//Liskov Substitution Principle (LSP): BookServiceImpl implements the PublicationService interface, ensuring that an
// instance of BookServiceImpl can replace the PublicationService wherever it's used.

//Interface Segregation Principle (ISP): BookServiceImpl implements only the methods it needs from the PublicationService interface,
// ensuring no unnecessary methods are implemented.

//Dependency Inversion Principle (DIP): The BookServiceImpl class depends on the abstraction (PublicationService interface)
// and not on the concrete implementation. This makes the system more flexible and easier to manage.






// Importing necessary classes and interfaces.
import models.Publication;
import java.util.ArrayList;
import java.util.List;

// The 'BookServiceImpl' class implements the 'PublicationService' interface.
// This class is responsible for managing the operations related to books.
public class BookServiceImpl implements PublicationService {

    // A private list to store books.
    private List<Publication> bookList = new ArrayList<>();

    // Overriding the 'addPublication' method from the 'PublicationService' interface.
    // This method adds a new publication (book) to the list.
    @Override
    public void addPublication(Publication publication) {
        bookList.add(publication);
    }

    // Overriding the 'listPublications' method from the 'PublicationService' interface.
    // This method returns the list of all books.
    @Override
    public List<Publication> listPublications() {
        return bookList;
    }
}
