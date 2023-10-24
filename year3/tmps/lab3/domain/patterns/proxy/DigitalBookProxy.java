package domain.patterns.proxy;

// Proxy class controlling access to the RealDigitalBook
public class DigitalBookProxy implements DigitalBook {
    private String title;
    private RealDigitalBook realDigitalBook;
    private boolean hasLicense;

    public DigitalBookProxy(String title, boolean hasLicense) {
        this.title = title;
        this.hasLicense = hasLicense;
    }

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
