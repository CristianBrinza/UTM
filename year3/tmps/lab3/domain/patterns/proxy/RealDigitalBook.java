package domain.patterns.proxy;

// Real implementation of the DigitalBook interface
public class RealDigitalBook implements DigitalBook {
    private String title;

    public RealDigitalBook(String title) {
        this.title = title;
        loadFromDisk();
    }

    private void loadFromDisk() {
        System.out.println("Loading book from disk: " + title);
    }

    @Override
    public void read() {
        System.out.println("Reading book: " + title);
    }
}
