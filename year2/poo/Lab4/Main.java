
import src.Customer;
import src.Consultant;
import src.Order;
import src.Librarian;
import src.Library;
import src.Product;
import src.Security;
import src.SupplementDelivery;

public class Main {
    public static void main(String[] args) {
        // Scenario 1: Customer orders products which do not need order
        System.out.println(" ");
        System.out.println("===================================================================");
        System.out.println("Scenario 1: Customer orders products which do not need order");
        System.out.println("Variations:");
        System.out.println("- The product is in stock");
        System.out.println("- One of the products is less in stock than customer needs");
        System.out.println("- The product is out of stock");
        System.out.println("==================================================================");
        var Library1 = new Library();
        var Librarian1 = new Librarian();
        Library1.setLibrarian(Librarian1);
        var DeliveryCar1 = new SupplementDelivery();
        Library1.setDeliveryCar(DeliveryCar1);
        var Product1 = new Product(10, 4.5, 20);
        var Product2 = new Product(12, 7, 12);
        var Product3 = new Product(12, 9.7, 5);
        Library1.supplyStock(Product1);
        Library1.supplyStock(Product2);
        var Customer1 = new Customer();
        Customer1.comeToLibrary(Library1, new Order());
        Customer1.addProductToOrder(Product1, 3);
        Customer1.addProductToOrder(Product2, 35);
        Customer1.addProductToOrder(Product3, 5);
        Customer1.finishOrder();

        // Scenario 2: Customer orders a products which need orders
        System.out.println(" ");
        System.out.println("============================================================");
        System.out.println("Scenario 2: Customer orders products which need oreder");
        System.out.println("Variations:");
        System.out.println("- Client has the needed order");
        System.out.println("- Client doesn't have the needed order");
        System.out.println("============================================================");
        var Library2 = new Library();
        var Librarian2 = new Librarian();
        Library2.setLibrarian(Librarian1);
        var DeliveryCar2 = new SupplementDelivery();
        Library2.setDeliveryCar(DeliveryCar2);
        var Product4 = new Product(10, 4.5, 20, true);
        var Product5 = new Product(12, 9.7, 5, true);
        Library2.supplyStock(Product4);
        Library2.supplyStock(Product5);
        var Customer2 = new Customer();
        var Doctor2 = new Consultant();
        Doctor2.suggestbook(Customer2, Product4);
        Customer2.comeToLibrary(Library2, new Order());
        Customer2.addProductToOrder(Product4, 2);
        Customer2.addProductToOrder(Product5, 2);
        Customer2.finishOrder();

        // Scenario 3: Customer tries to rob the library:
        System.out.println(" ");
        System.out.println("============================================================");
        System.out.println("Scenario 3: Customer tries to rob the library");
        System.out.println("Variations:");
        System.out.println("- Client is arrested (with probability of 80%)");
        System.out.println("- Client is not arrested");
        System.out.println("============================================================");
        var Library3 = new Library();
        var Librarian3 = new Librarian();
        Library3.setLibrarian(Librarian3);
        var DeliveryCar3 = new SupplementDelivery();
        Library3.setDeliveryCar(DeliveryCar3);
        var SecurityCar3 = new Security();
        Library3.setSecurityCar(SecurityCar3);
        var Customer3 = new Customer();
        Customer3.comeToLibrary(Library3, new Order());
        Customer3.robLibrary();

    }
}