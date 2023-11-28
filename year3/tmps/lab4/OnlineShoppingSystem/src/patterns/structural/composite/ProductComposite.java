package patterns.structural.composite;

import java.util.ArrayList;
import java.util.List;

// Composite: Defines behavior for components having children and stores child components.
public class ProductComposite extends ProductComponent {
    private List<ProductComponent> productComponents = new ArrayList<>();
    private String groupName;

    public ProductComposite(String groupName) {
        this.groupName = groupName;
    }

    @Override
    public void add(ProductComponent productComponent) {
        productComponents.add(productComponent);
    }

    @Override
    public void remove(ProductComponent productComponent) {
        productComponents.remove(productComponent);
    }

    @Override
    public void displayProductInfo() {
        System.out.println("Category: " + groupName);
        for (ProductComponent productComponent : productComponents) {
            productComponent.displayProductInfo();
        }
    }
}
