// This package 'domain' focuses on the business operations linked to publications.
package domain;




//Single Responsibility Principle (SRP): MagazineServiceImpl has one clear responsibility: to manage operations related to
// magazines. It maintains a list of magazines and provides methods to add to and list those magazines.

//Open/Closed Principle (OCP): MagazineServiceImpl is an implementation of the PublicationService interface. If there's a need
// to introduce new functionalities specific to magazines in the future, we can do so in this class without modifying the interface.

//Liskov Substitution Principle (LSP): MagazineServiceImpl implements the PublicationService interface, ensuring that an instance
// of MagazineServiceImpl can replace the PublicationService wherever it's used.

//Interface Segregation Principle (ISP): MagazineServiceImpl implements only the methods it needs from the PublicationService
// interface, ensuring no unnecessary methods are implemented.

//Dependency Inversion Principle (DIP): The MagazineServiceImpl class depends on the abstraction (PublicationService interface)
// and not on the concrete implementation. This makes the system more flexible and easier to manage.







// Importing necessary classes and interfaces.
import models.Publication;
import java.util.ArrayList;
import java.util.List;

// The 'MagazineServiceImpl' class implements the 'PublicationService' interface.
// This class is responsible for managing the operations related to magazines.
public class MagazineServiceImpl implements PublicationService {

    // A private list to store magazines.
    private List<Publication> magazineList = new ArrayList<>();

    // Overriding the 'addPublication' method from the 'PublicationService' interface.
    // This method adds a new publication (magazine) to the list.
    @Override
    public void addPublication(Publication publication) {
        magazineList.add(publication);
    }

    // Overriding the 'listPublications' method from the 'PublicationService' interface.
    // This method returns the list of all magazines.
    @Override
    public List<Publication> listPublications() {
        return magazineList;
    }
}
