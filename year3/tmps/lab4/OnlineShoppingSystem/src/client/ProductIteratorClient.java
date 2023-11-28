package client;
/*


ProductIterator: This is the iterator interface that defines methods for traversing over elements.
ProductCollection: An aggregate interface that declares a method for creating an iterator.
ProductListCollection: A concrete implementation of the ProductCollection interface. It uses an internal list to store products and provides an iterator for traversing this list.
Product: A simple domain class representing a product.
ProductIteratorClient: This client class demonstrates the use of the Iterator pattern to iterate over a collection of products.

*/


import domain.products.Product;
import patterns.behavioral.iterator.ProductCollection;
import patterns.behavioral.iterator.ProductIterator;
import patterns.behavioral.iterator.ProductListCollection;

// Client code to demonstrate use of Iterator pattern
public class ProductIteratorClient {
    public static void main(String[] args) {
        ProductCollection products = new ProductListCollection();
        ((ProductListCollection) products).addProduct((domain.Product) new Product("Smartphone"));
        ((ProductListCollection) products).addProduct((domain.Product) new Product("Laptop"));
        ((ProductListCollection) products).addProduct((domain.Product) new Product("Tablet"));

        ProductIterator iterator = products.createIterator();
        while (iterator.hasNext()) {
            Product product = (Product) iterator.next();
            System.out.println("Product: " + product.getName());
        }
    }
}

