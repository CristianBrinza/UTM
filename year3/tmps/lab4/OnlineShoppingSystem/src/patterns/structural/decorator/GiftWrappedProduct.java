package patterns.structural.decorator;


import domain.Product;

// Concrete Decorator for adding gift wrapping
public class GiftWrappedProduct extends ProductDecorator {
    public GiftWrappedProduct(Product decoratedProduct) {
        super(decoratedProduct);
    }

    @Override
    public String getName() {
        return null;
    }

    @Override
    public String getDescription() {
        return super.getDescription() + ", Gift Wrapped";
    }

    @Override
    public double getPrice() {
        return super.getPrice() + 5.00; // Adding a fixed price for gift wrapping
    }

    @Override
    public void describeProduct() {

    }

    @Override
    public Product cloneProduct() {
        return null;
    }
}

