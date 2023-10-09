/**
 * EBook Class
 *
 * Description: Represents an electronic book.
 * Design Pattern: N/A
 */
public class EBook implements Book {
    private final String title;
    private final String authorName;

    // Constructor initializes the eBook with title and author.
    public EBook(String title, String authorName) {
        this.title = title;
        this.authorName = authorName;
    }

    // Getter for the title of the eBook.
    @Override
    public String getTitle() {
        return title;
    }

    // Getter for the author name of the eBook.
    @Override
    public String getAuthorName() {
        return authorName;
    }
}
