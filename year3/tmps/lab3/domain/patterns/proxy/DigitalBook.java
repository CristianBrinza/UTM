//   The DigitalBookProxy class implements the DigitalBook interface.

//   It contains attributes for the title, the actual 'RealDigitalBook' object, 
//and a boolean flag to check if the book has a license.

//   The read() method checks if the book has a license. If it does, it initializes 
//the RealDigitalBook (if not already done) and delegates the reading operation to it. 

//   If the book doesn't have a license, it prints a message indicating the same.


package domain.patterns.proxy;

/**
 * Interface representing digital books.
 * This interface defines the structure for digital books
 * and serves as a contract for any class that wants to act
 * as a digital book, whether it's a real digital book or its proxy.
 */
public interface DigitalBook {
    /**
     * Simulates reading the digital book.
     */
    void read();
}