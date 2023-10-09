/**
 * PrintBook Class
 *
 * Description: Represents a physical print book.
 * Design Pattern: N/A
 */
public class PrintBook implements Book {
    private final String title;
    private final String authorName;

    // Constructor initializes the print book with title and author.
    public PrintBook(String title, String authorName) {
        this.title = title;
        this.authorName = authorName;
    }

    // Getter for the title of the print book.
    @Override
    public String getTitle() {
        return title;
    }

    // Getter for the author name of the print book.
    @Override
    public String getAuthorName() {
        return authorName;
    }
}
