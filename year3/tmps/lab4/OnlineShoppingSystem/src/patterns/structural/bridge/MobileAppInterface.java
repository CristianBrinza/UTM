package patterns.structural.bridge;

// Concrete Implementation of a mobile app-based user interface
public class MobileAppInterface implements UserInterface {
    @Override
    public void displayProduct(String product) {
        System.out.println("Displaying " + product + " on the mobile app interface.");
        // Mobile app interface specific rendering logic
    }
}

