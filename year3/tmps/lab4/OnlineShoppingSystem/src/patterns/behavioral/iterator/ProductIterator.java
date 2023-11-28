package patterns.behavioral.iterator;


import domain.Product;

// Iterator interface for products
public interface ProductIterator {
    boolean hasNext();
    Product next();
}

