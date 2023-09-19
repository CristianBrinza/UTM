package domain;

import factory.AbstractFactory;
import factory.BookFactory;
import factory.TransactionFactory;
import factory.UserFactory;
import models.IBook;
import models.Transaction;
import models.User;

import java.util.ArrayList;
import java.util.List;

public class Library {
    private List<IBook> books;
    private List<User> users;
    private List<Transaction> transactions;
    private BookFactory bookFactory;
    private AbstractFactory<User> userFactory;
    private AbstractFactory<Transaction> transactionFactory;

    // DIP: Depend upon abstraction. Constructors now expect factories that adhere to the AbstractFactory interface.
    public Library() {
        this.bookFactory = new BookFactory();
        this.userFactory = new UserFactory();
        this.transactionFactory = new TransactionFactory();
        this.books = new ArrayList<>();
        this.users = new ArrayList<>();
        this.transactions = new ArrayList<>();
    }

    public IBook getBookByTitle(String title) {
        for (IBook book : books) {
            if (book.getTitle().equals(title)) {
                return book;
            }
        }
        return null; // or throw an exception if the book is not found
    }

    public User getUserByName(String name) {
        for (User user : users) {
            if (user.getName().equals(name)) {
                return user;
            }
        }
        return null; // or throw an exception if the user is not found
    }

    public void addBook(String title, String author) {
        IBook book = bookFactory.create(books.size() + 1, title, author);
        books.add(book);


    // Rest of the class remains the same...
}

    public void addUser(String name) {
        User user = userFactory.create(users.size() + 1, name);
        users.add(user);
    }
    public void issueBook(User user, IBook book) {
        // Check if the book is available
        if(!books.contains(book)) {
            throw new IllegalStateException("Book is not available");
        }

        // Check if the user is registered
        if(!users.contains(user)) {
            throw new IllegalStateException("User is not registered");
        }

        // Create a transaction
        Transaction transaction = transactionFactory.create(user, book);
        transactions.add(transaction);

        // Remove the issued book from available books
        books.remove(book);
    }





}
