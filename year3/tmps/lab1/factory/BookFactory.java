package factory;

import models.Book;

public class BookFactory implements AbstractFactory<Book> {
    // OCP: Allow dynamic creation of a book based on passed arguments.
    @Override
    public Book create(Object... args) {
        if(args.length < 3) {
            throw new IllegalArgumentException("Not enough arguments to create a book");
        }
        int id = (int) args[0];
        String title = (String) args[1];
        String author = (String) args[2];
        return new Book(id, title, author);
    }
}
