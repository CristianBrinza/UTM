package domain.patterns.adapter;

public class PrinterAdapter {
    private ThirdPartyPrinter thirdPartyPrinter;

    // Constructor to initialize the third-party printer
    public PrinterAdapter(ThirdPartyPrinter thirdPartyPrinter) {
        this.thirdPartyPrinter = thirdPartyPrinter;
    }

    // Method that our system uses to request prints
    public void requestPrint(String bookContent) {
        // Use the third-party printer's method to print
        thirdPartyPrinter.executePrintJob(bookContent);
    }
}
