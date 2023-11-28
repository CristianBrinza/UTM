package domain.products;



import patterns.structural.flyweight.ProductFlyweight;

// Context class using the Flyweight pattern for product type data
public class ProductDetail {
    private String productName;
    private double price;
    private ProductFlyweight productTypeData;

    public ProductDetail(String productName, double price, ProductFlyweight productTypeData) {
        this.productName = productName;
        this.price = price;
        this.productTypeData = productTypeData;
    }

    public void displayProductInfo() {
        System.out.println("Product: " + productName + ", Price: $" + price);
        productTypeData.displayProductTypeData();
    }
}
