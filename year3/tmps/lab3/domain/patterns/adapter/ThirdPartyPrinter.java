package domain.patterns.adapter;

/**
 * Represents a third-party printer service.
 * This class simulates a printer that our system does not have direct compatibility with.
 */
public class ThirdPartyPrinter {
    
    /**
     * Method that the third-party printing service expects to execute print jobs.
     * 
     * @param bookContent Content of the book to be printed.
     */
    public void executePrintJob(String bookContent) {
        System.out.println("Printing book using ThirdPartyPrinter: " + bookContent);
    }
}