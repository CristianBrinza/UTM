package patterns.structural.bridge;


// Concrete Implementation of a web-based user interface
public class WebInterface implements UserInterface {
    @Override
    public void displayProduct(String product) {
        System.out.println("Displaying " + product + " on the web interface.");
        // Web interface specific rendering logic
    }
}

