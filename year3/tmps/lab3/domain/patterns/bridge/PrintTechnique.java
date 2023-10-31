package domain.patterns.bridge;

/**
 * Interface representing the abstraction for various printing techniques.
 * This interface serves as the abstraction that can be implemented by 
 * different concrete printing techniques like digital print, screen print, etc.
 */
public interface PrintTechnique {
    /**
     * Simulates printing the given content using the specific printing technique.
     * 
     * @param content Content to be printed.
     */
    void print(String content);
}