package domain.patterns.bridge;

// Concrete implementation of PrintTechnique using screen printing
public class ScreenPrint implements PrintTechnique {
    @Override
    public void print(String content) {
        System.out.println("Printing using Screen Print: " + content);
    }
}
