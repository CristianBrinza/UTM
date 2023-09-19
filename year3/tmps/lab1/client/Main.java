package client;

import domain.Library;
import models.Book;
import models.User;

public class Main {
    public static void main(String[] args) {
        Library library = new Library();

        library.addBook("Moby Dick", "Herman Melville");
        library.addBook("The Great Gatsby", "F. Scott Fitzgerald");

        library.addUser("Alice");
        library.addUser("Bob");

        Book book1 = new Book(1, "Moby Dick", "Herman Melville");
        User user1 = new User(1, "Alice");

        library.issueBook(user1, book1);

        // Add more operations as needed.
    }
}
