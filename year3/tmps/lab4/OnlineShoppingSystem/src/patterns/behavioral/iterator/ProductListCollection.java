package patterns.behavioral.iterator;


import domain.Product;
import java.util.ArrayList;
import java.util.List;

// Concrete Aggregate implementing ProductCollection
public class ProductListCollection implements ProductCollection {
    private List<Product> productList = new ArrayList<>();

    public void addProduct(Product product) {
        productList.add(product);
    }

    @Override
    public ProductIterator createIterator() {
        return new ProductListIterator();
    }

    private class ProductListIterator implements ProductIterator {
        private int currentIndex = 0;

        @Override
        public boolean hasNext() {
            return currentIndex < productList.size();
        }

        @Override
        public Product next() {
            return productList.get(currentIndex++);
        }
    }
}

