package domain.patterns.proxy;

/**
 * RealDigitalBook is the actual class that represents a digital book.
 * It implements the DigitalBook interface and contains the logic to 
 * simulate loading and reading a digital book.
 */
public class RealDigitalBook implements DigitalBook {
    private String title;  // Title of the digital book

    /**
     * Constructor for RealDigitalBook. It initializes the book title
     * and simulates loading the book from the disk.
     *
     * @param title Title of the digital book.
     */
    public RealDigitalBook(String title) {
        this.title = title;
        loadFromDisk();
    }

    /**
     * Private method to simulate loading the digital book from disk.
     */
    private void loadFromDisk() {
        System.out.println("Loading book from disk: " + title);
    }

    /**
     * Implements the read method from DigitalBook interface.
     * Simulates reading the digital book.
     */
    @Override
    public void read() {
        System.out.println("Reading book: " + title);
    }
}