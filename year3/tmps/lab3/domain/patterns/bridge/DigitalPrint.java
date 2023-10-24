package domain.patterns.bridge;

// Concrete implementation of PrintTechnique using digital printing

// A concrete implementation of the PrintTechnique interface which simulates digital printing.
public class DigitalPrint implements PrintTechnique {
    @Override
    public void print(String content) {
        System.out.println("Printing using Digital Print: " + content);
    }
}
