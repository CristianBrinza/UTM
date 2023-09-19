package models;

import java.util.Date;

// SRP: Represents a single entity, a transaction.
public class Transaction {
    private int id;
    private User user;
    private Book book;
    private Date issuedDate;
    private Date returnDate;

    public Transaction(int id, User user, Book book, Date issuedDate) {
        this.id = id;
        this.user = user;
        this.book = book;
        this.issuedDate = issuedDate;
        this.returnDate = null;
    }

    public Transaction(User user, IBook book) {
    }

    public int getId() { return id; }
    public User getUser() { return user; }
    public Book getBook() { return book; }
    public Date getIssuedDate() { return issuedDate; }
    public Date getReturnDate() { return returnDate; }

    public void setReturnDate(Date returnDate) { this.returnDate = returnDate; }
}
