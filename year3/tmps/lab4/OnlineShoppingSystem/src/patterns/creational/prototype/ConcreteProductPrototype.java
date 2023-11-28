package patterns.creational.prototype;

public class ConcreteProductPrototype implements ProductPrototype {
    private String productType;

    public ConcreteProductPrototype(String productType) {
        this.productType = productType;
    }

    @Override
    public ProductPrototype cloneProduct() {
        return new ConcreteProductPrototype(this.productType);
    }

    public void displayProductType() {
        System.out.println("Product Type: " + productType);
    }
}
