/**
 * Client Class
 *
 * Description: Demonstrates the usage of the implemented design patterns.
 * Design Pattern: N/A
 */
public class Client {
    public static void main(String[] args) {
        // Get the single instance of the publishing manager.
        PublishingManager publishingManager = PublishingManager.getInstance();

        // Create books using the publishing manager.
        Book eBook = publishingManager.createBook("EBook", "Digital World", "Alice");
        Book printBook = publishingManager.createBook("PrintBook", "Paper Trails", "Bob");

        // Build a publishing house using the Builder pattern.
        PublishingHouse publishingHouse = new PublishingHouse.Builder()
                .setEBook(eBook)
                .setPrintBook(printBook)
                .build();

        // Display information about the books in the publishing house.
        publishingHouse.displayBooks();

        // Clone an author using the Prototype pattern.
        AuthorPrototype author = new FictionAuthor("Author Carol");
        AuthorPrototype newAuthor = author.clone();

        // Display information about the original and cloned authors.
        System.out.println("Original Author: " + author.getName());
        System.out.println("Cloned Author: " + newAuthor.getName());
    }
}
