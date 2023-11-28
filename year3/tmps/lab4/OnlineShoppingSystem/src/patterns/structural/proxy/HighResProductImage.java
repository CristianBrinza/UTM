package patterns.structural.proxy;


// Real Subject class that is resource-intensive
public class HighResProductImage implements ProductImage {
    private String imagePath;

    public HighResProductImage(String imagePath) {
        this.imagePath = imagePath;
        loadFromDisk(); // Simulates the delay in loading a high-resolution image
    }

    private void loadFromDisk() {
        System.out.println("Loading " + imagePath);
        // Actual loading code goes here
    }

    @Override
    public void displayImage() {
        System.out.println("Displaying " + imagePath);
    }
}

