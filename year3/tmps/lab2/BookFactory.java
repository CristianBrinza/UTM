/**
 * BookFactory Class
 *
 * Description: Responsible for creating book objects.
 * Design Pattern: Factory Method - This pattern provides an interface for creating
 *                instances of a class, with its subclasses deciding which class to instantiate.
 */
public class BookFactory {
    // Method creates a book of a specific type (eBook or print book).
    public Book createBook(String type, String title, String authorName) {
        switch (type.toLowerCase()) {
            case "ebook":
                return new EBook(title, authorName);
            case "printbook":
                return new PrintBook(title, authorName);
            default:
                throw new IllegalArgumentException("Invalid book type");
        }
    }
}
