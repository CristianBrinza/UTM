package patterns.structural.proxy;

// Proxy class for HighResProductImage
public class ProductImageProxy implements ProductImage {
    private HighResProductImage highResProductImage;
    private String imagePath;

    public ProductImageProxy(String imagePath) {
        this.imagePath = imagePath;
    }

    @Override
    public void displayImage() {
        if (highResProductImage == null) {
            highResProductImage = new HighResProductImage(imagePath); // Load image on-demand
        }
        highResProductImage.displayImage();
    }
}

