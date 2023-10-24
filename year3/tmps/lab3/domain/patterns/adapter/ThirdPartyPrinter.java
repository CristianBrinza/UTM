package domain.patterns.adapter;

public class ThirdPartyPrinter {
    // Method that the third-party printing service expects
    public void executePrintJob(String bookContent) {
        // Logic to print the book content
        System.out.println("Printing book using ThirdPartyPrinter: " + bookContent);
    }
}
