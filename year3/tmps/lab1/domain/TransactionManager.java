package domain;

import models.Transaction;
import factory.AbstractFactory;

import java.util.ArrayList;
import java.util.List;

public class TransactionManager {
    private List<Transaction> transactions;
    private AbstractFactory<Transaction> transactionFactory;

    public TransactionManager(AbstractFactory<Transaction> transactionFactory) {
        this.transactions = new ArrayList<>();
        this.transactionFactory = transactionFactory;
    }

    public void addTransaction(Transaction transaction) {
        transactions.add(transaction);
    }

    // Other transaction related methods can be added here
}
