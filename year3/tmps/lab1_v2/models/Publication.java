// This is the package declaration. All the classes and interfaces within this directory belong to the 'models' package.
package models;




//Single Responsibility Principle (SRP): The Publication interface is focused solely on the essential
// attributes of a publication, keeping its responsibility limited and singular.


//Liskov Substitution Principle (LSP): The interface ensures a contract. Any class implementing this interface
// can be substituted wherever a Publication is expected.



// The 'Publication' interface declaration.
// An interface in Java is a reference type, similar to a class, that is used to define the contract (i.e., a set of abstract methods)
// that classes can implement. Implementing an interface allows a class to inherit the abstract methods of the interface.
public interface Publication {

	// Abstract method to get the title of the publication.
	// Classes that implement the 'Publication' interface must provide an implementation for this method.
	String getTitle();

	// Abstract method to get the author of the publication.
	// Classes that implement the 'Publication' interface must provide an implementation for this method.
	String getAuthor();

	// Abstract method to get the ISBN (International Standard Book Number) of the publication.
	// Classes that implement the 'Publication' interface must provide an implementation for this method.
	String getISBN();

	// Abstract method to get the type of the publication (e.g., book, magazine).
	// Classes that implement the 'Publication' interface must provide an implementation for this method.
	String getType();
}
