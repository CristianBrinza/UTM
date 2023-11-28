package patterns.behavioral.iterator;


// Aggregate interface for product collections
public interface ProductCollection {
    ProductIterator createIterator();
}

