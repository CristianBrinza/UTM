package domain.patterns.adapter;

/**
 * Adapter class that provides compatibility between our system and the ThirdPartyPrinter.
 * This class uses composition to hold an instance of ThirdPartyPrinter and bridges the gap 
 * between our system's printing method and the third-party printer's method.
 */
public class PrinterAdapter {
    private ThirdPartyPrinter thirdPartyPrinter;  // Instance of the third-party printer

    /**
     * Constructor to initialize the third-party printer.
     * 
     * @param thirdPartyPrinter Instance of the third-party printer.
     */
    public PrinterAdapter(ThirdPartyPrinter thirdPartyPrinter) {
        this.thirdPartyPrinter = thirdPartyPrinter;
    }

    /**
     * Method that our system uses to request printing jobs.
     * Internally, this method delegates the print request to the third-party printer's method.
     * 
     * @param bookContent Content of the book to be printed.
     */
    public void requestPrint(String bookContent) {
        thirdPartyPrinter.executePrintJob(bookContent);
    }
}