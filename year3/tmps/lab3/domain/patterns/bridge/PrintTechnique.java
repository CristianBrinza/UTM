package domain.patterns.bridge;

// Interface representing the abstraction for printing techniques

// PrintTechnique Interface:
// This interface serves as the abstraction for various printing techniques.
// It defines a single method print() which takes the content to be printed.
public interface PrintTechnique {
    void print(String content);
}
