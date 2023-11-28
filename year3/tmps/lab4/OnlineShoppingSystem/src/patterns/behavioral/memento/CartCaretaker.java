package patterns.behavioral.memento;


// Caretaker class
public class CartCaretaker {
    private CartMemento memento;

    public void saveCart(ShoppingCart cart) {
        memento = cart.save();
    }

    public void restoreCart(ShoppingCart cart) {
        cart.restore(memento);
    }
}

