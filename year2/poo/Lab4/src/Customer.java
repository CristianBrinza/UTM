package src;

import java.util.ArrayList;

public final class Customer extends Root implements ClientInterface {

    private final ArrayList<Integer> recomandation = new ArrayList<Integer>();

    private LibraryInterface library;
    private OrderInterface order;
    // private ProductInterface currentProduct;

    public Customer() {
        this.id = generateId();
        objectsCount += 1;
    }

    public void comeToLibrary(LibraryInterface library, OrderInterface order) {
        this.library = library;
        this.order = order;
        System.out.println(" ");
        System.out.println("Client with id " + this.id + " came to library with id " + library.getId());
        System.out.println("Order with id " + order.getId() + " is assigned to this client");
    }

    public void addProductToOrder(ProductInterface product, int amount) {
        System.out.println(" ");
        if (product.getOrderNeeded()) {
            library.checkOrder(this.hasOrder(product.getId()));
            if (!this.hasOrder(product.getId())) {
                return;
            }
        }
        int stock = library.checkStock(product, amount);
        if (stock == 0) {
        } else {
            this.order.addProducts(product, stock);
            this.library.removeStock(product, stock);
            this.library.addCash(this.order.getOrderRevenue());
        }
    }

    public void finishOrder() {
        System.out.println(" ");
        System.out.println("The client finalized the order");
        this.order.printOrderStats();
    }

    public void robLibrary() {
        this.library.robCashRegister();
    }

    public boolean hasOrder(int id) {
        return recomandation.contains(id);
    }

    @Override
    public void addOrder(int bookId) {
        recomandation.add(bookId);
    }

    @Override
    public int getId() {
        return this.id;
    }
}
