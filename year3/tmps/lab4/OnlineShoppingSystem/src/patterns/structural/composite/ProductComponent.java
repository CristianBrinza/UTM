package patterns.structural.composite;


// Component: Declares the interface for objects in the composition.
public abstract class ProductComponent {
    public void add(ProductComponent productComponent) {
        throw new UnsupportedOperationException();
    }

    public void remove(ProductComponent productComponent) {
        throw new UnsupportedOperationException();
    }

    public String getName() {
        throw new UnsupportedOperationException();
    }

    public double getPrice() {
        throw new UnsupportedOperationException();
    }

    public void displayProductInfo() {
        throw new UnsupportedOperationException();
    }
}

