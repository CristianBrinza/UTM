package patterns.creational.builder;

public class Product {
    private String partA;
    private String partB;

    public void setPartA(String partA) {
        this.partA = partA;
    }

    public void setPartB(String partB) {
        this.partB = partB;
    }

    public void showProduct() {
        System.out.println("Product Parts: " + partA + ", " + partB);
    }
}

