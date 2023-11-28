package client;


import patterns.structural.proxy.ProductImageProxy;

// Client code that interacts with the Proxy
public class ProductViewer {
    public static void main(String[] args) {
        ProductImageProxy imageProxy = new ProductImageProxy("product1.jpg");
        // Image is not loaded in memory yet

        // Image loading happens only when required
        imageProxy.displayImage(); // At this point, the real image will be loaded and displayed
    }
}

