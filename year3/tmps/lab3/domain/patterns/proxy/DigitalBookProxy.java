package domain.patterns.proxy;

/**
 * DigitalBookProxy is the proxy class that controls access to RealDigitalBook.
 * It implements the DigitalBook interface and checks if the user has a license
 * to read the digital book before granting access.
 */
public class DigitalBookProxy implements DigitalBook {
    private String title;               // Title of the digital book
    private RealDigitalBook realDigitalBook;  // Reference to the real digital book
    private boolean hasLicense;         // Flag to check if user has a license to read the book

    /**
     * Constructor for DigitalBookProxy.
     *
     * @param title      Title of the digital book.
     * @param hasLicense Flag indicating if the user has a license to read the book.
     */
    public DigitalBookProxy(String title, boolean hasLicense) {
        this.title = title;
        this.hasLicense = hasLicense;
    }

    /**
     * Implements the read method from DigitalBook interface.
     * Checks if the user has a license to read the book.
     * If they do, it loads the real digital book (if not already loaded)
     * and simulates reading. If not, it denies access.
     */
    @Override
    public void read() {
        if (hasLicense) {
            if (realDigitalBook == null) {
                realDigitalBook = new RealDigitalBook(title);
            }
            realDigitalBook.read();
        } else {
            System.out.println("Cannot read book. License is missing for: " + title);
        }
    }
}