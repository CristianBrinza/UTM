package patterns.structural.decorator;


import domain.Product;

// Concrete Decorator for adding insurance
public class InsuredProduct extends ProductDecorator {
    public InsuredProduct(Product decoratedProduct) {
        super(decoratedProduct);
    }

    @Override
    public String getName() {
        return null;
    }

    @Override
    public String getDescription() {
        return super.getDescription() + ", Insured";
    }

    @Override
    public double getPrice() {
        return super.getPrice() + 20.00; // Adding a fixed price for insurance
    }

    @Override
    public void describeProduct() {

    }

    @Override
    public Product cloneProduct() {
        return null;
    }
}
