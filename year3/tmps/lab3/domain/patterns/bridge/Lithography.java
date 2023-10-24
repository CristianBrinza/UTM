package domain.patterns.bridge;

// Concrete implementation of PrintTechnique using lithography

// A concrete implementation of the PrintTechnique interface which simulates lithographic printing.
public class Lithography implements PrintTechnique {
    @Override
    public void print(String content) {
        System.out.println("Printing using Lithography: " + content);
    }
}
