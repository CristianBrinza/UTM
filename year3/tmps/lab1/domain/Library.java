package domain;

import factory.AbstractFactory;
import models.IBook;
import models.Transaction;
import models.User;

import java.util.ArrayList;
import java.util.List;

public class Library {
    private List<IBook> books;
    private List<User> users;
    private List<Transaction> transactions;
    private AbstractFactory<IBook> bookFactory;
    private AbstractFactory<User> userFactory;
    private AbstractFactory<Transaction> transactionFactory;

    // DIP: Depend upon abstraction. Constructors now expect factories that adhere to the AbstractFactory interface.
    public Library(AbstractFactory<IBook> bookFactory, AbstractFactory<User> userFactory, AbstractFactory<Transaction> transactionFactory) {
        this.books = new ArrayList<>();
        this.users = new ArrayList<>();
        this.transactions = new ArrayList<>();
        this.bookFactory = bookFactory;
        this.userFactory = userFactory;
        this.transactionFactory = transactionFactory;
    }

    public Library() {

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
