package client;

import domain.Library;
import factory.AbstractFactory;
import factory.BookFactory;
import factory.TransactionFactory;
import factory.UserFactory;
import models.IBook;
import models.Transaction;
import models.User;

public class Main {
    public static void main(String[] args) {
        BookFactory bookFactory = new BookFactory();
        AbstractFactory<User> userFactory = new UserFactory();
        AbstractFactory<Transaction> transactionFactory = new TransactionFactory();

        Library library = new Library();

        library.addBook("Moby Dick", "Herman Melville");
        library.addBook("The Great Gatsby", "F. Scott Fitzgerald");

        library.addUser("Alice");
        library.addUser("Bob");

        // Instead of creating a new instance, retrieve the book and user from the library
        IBook book1 = library.getBookByTitle("Moby Dick"); // You'll need to implement this method in the Library class
        User user1 = library.getUserByName("Alice");       // You'll need to implement this method in the Library class

        library.issueBook(user1, book1);

        // Add more operations as needed.
    }
}
