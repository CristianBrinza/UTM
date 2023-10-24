package domain.models;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Order {
    private Date orderDate;              // Date when the order was placed
    private List<Book> orderedBooks;     // List of books in the order
    private double totalPrice;           // Total price of the order

    // Constructor to initialize an order with a list of books
    public Order(List<Book> orderedBooks) {
        this.orderDate = new Date();  // Set to the current date/time
        this.orderedBooks = orderedBooks;
        this.totalPrice = calculateTotalPrice();  // Calculate the total price of the order
    }

    // Private method to calculate the total price of the order
    private double calculateTotalPrice() {
        double total = 0.0;
        for (Book book : orderedBooks) {
            total += book.getPrice();  // Add up the prices of all books in the order
        }
        return total;
    }

    // Getter method to retrieve the date of the order
    public Date getOrderDate() {
        return orderDate;
    }

    // Getter method to retrieve the list of books in the order
    // We return a copy of the list to ensure encapsulation and immutability
    public List<Book> getOrderedBooks() {
        return new ArrayList<>(orderedBooks);
    }

    // Getter method to retrieve the total price of the order
    public double getTotalPrice() {
        return totalPrice;
    }
}
