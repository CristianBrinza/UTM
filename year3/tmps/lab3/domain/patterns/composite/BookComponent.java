package domain.patterns.composite;

// Interface representing the component for both individual books and collections
public interface BookComponent {
    double getPrice();
    void printDetails();
}
