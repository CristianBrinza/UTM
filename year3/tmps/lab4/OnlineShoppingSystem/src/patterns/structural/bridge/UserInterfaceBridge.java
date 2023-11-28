package patterns.structural.bridge;

// Bridge class that decouples the user interface abstraction from its implementation
public class UserInterfaceBridge {
    private UserInterface userInterface;

    public UserInterfaceBridge(UserInterface userInterface) {
        this.userInterface = userInterface;
    }

    public void showProduct(String product) {
        userInterface.displayProduct(product);
    }
}

