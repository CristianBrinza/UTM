// This package 'domain' focuses on the business operations linked to publications.
package domain;


//Single Responsibility Principle (SRP): The PublicationService interface has a clear responsibility:
// to provide a contract for services that manage publications.

//Open/Closed Principle (OCP): The PublicationService interface is open for extension (classes can implement it
// and provide their own logic) but closed for modification (the core interface itself should remain unchanged).

//Liskov Substitution Principle (LSP): Any class that implements the PublicationService interface should be
// able to be used wherever the PublicationService is expected.

//Interface Segregation Principle (ISP): The PublicationService interface is minimalistic and contains only the essential
// methods required for a publication service. Implementing classes are not burdened with unnecessary methods.

//Dependency Inversion Principle (DIP): The system depends on this interface (an abstraction) rather than concrete implementations,
// promoting flexibility and decoupling.







// Importing necessary classes.
import models.Publication;
import java.util.List;

// The 'PublicationService' interface declaration.
// This interface provides a contract for classes that manage publications, whether they are books, magazines, etc.
public interface PublicationService {

    // Abstract method declaration for adding a publication.
    // Implementing classes will provide their own version of this method.
    void addPublication(Publication publication);

    // Abstract method declaration for listing all publications.
    // Implementing classes will provide their own version of this method.
    List<Publication> listPublications();
}
