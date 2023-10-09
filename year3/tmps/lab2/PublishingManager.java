/**
 * PublishingManager Class
 *
 * Description: Manages the creation of books.
 * Design Pattern: Singleton - This pattern restricts a class from instantiating multiple objects.
 *                It is used where only a single instance of a class is required to control actions.
 */
public class PublishingManager {
    private static PublishingManager instance;
    private final BookFactory bookFactory;

    // Private constructor initializes the publishing manager and instantiates the book factory.
    private PublishingManager() {
        bookFactory = new BookFactory();
    }

    // Method gets the single instance of the publishing manager, creating it if it doesn't exist.
    public static PublishingManager getInstance() {
        if (instance == null) {
            instance = new PublishingManager();
        }
        return instance;
    }

    // Method creates a book using the book factory.
    public Book createBook(String type, String title, String authorName) {
        return bookFactory.createBook(type, title, authorName);
    }
}
