/**
 * PublishingHouse Class
 *
 * Description: Represents a publishing house that contains books.
 * Design Pattern: Builder - This pattern allows a client to construct a complex object
 *                step by step. It is especially useful when an object has a large number
 *                of parameters, some of which have defaults.
 */
public class PublishingHouse {
    private final Book eBook;
    private final Book printBook;

    // Nested static Builder class to facilitate the step-by-step creation of a publishing house object.
    public static class Builder {
        private Book eBook;
        private Book printBook;

        // Setter for the eBook, returns the Builder for chaining.
        public Builder setEBook(Book eBook) {
            this.eBook = eBook;
            return this;
        }

        // Setter for the print book, returns the Builder for chaining.
        public Builder setPrintBook(Book printBook) {
            this.printBook = printBook;
            return this;
        }

        // Method builds and returns a PublishingHouse object using the current state of the Builder.
        public PublishingHouse build() {
            return new PublishingHouse(this);
        }
    }

    // Private constructor initializes the publishing house with a Builder.
    private PublishingHouse(Builder builder) {
        this.eBook = builder.eBook;
        this.printBook = builder.printBook;
    }

    // Method displays information about the books in the publishing house.
    public void displayBooks() {
        System.out.println("Publishing House Books:");
        System.out.println("EBook: " + eBook.getTitle() + ", Author: " + eBook.getAuthorName());
        System.out.println("PrintBook: " + printBook.getTitle() + ", Author: " + printBook.getAuthorName());
    }
}
