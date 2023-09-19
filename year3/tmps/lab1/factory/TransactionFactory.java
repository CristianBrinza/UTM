package factory;

import models.Transaction;
import models.IBook;
import models.User;

public class TransactionFactory implements AbstractFactory<Transaction> {
    @Override
    public Transaction create(Object... args) {
        if(args.length < 2) {
            throw new IllegalArgumentException("Not enough arguments to create a transaction");
        }

        User user = (User) args[0];
        IBook book = (IBook) args[1];

        return new Transaction(user, book);
    }
}
