package Lab2;

import Lab2.src.*;

public class Main {

    public static void main(String[] args) {
        var Member1 = new Member("Ion");
        Member1.buyBook(8790, 5);

        // show all orders
        Member1.showOrders();


        // show number of costumers
        System.out.println("Number of customers: " + Member.memberCount);

        var Librarian1 = new Librarian("Vasile");
        Librarian1.sellBook(92490, 78942);



        Storage.addStats((float) 20000, (float) 5300, 20);
        Storage.addStats((float) 2050, (float) 570, 5);
        Storage.printReport();


        var Carturaresti = new Typography("Carturaresti");
        Carturaresti.addBook(56787);
        Carturaresti.addBook(67879);
        System.out.println("The list of all products of the " + Carturaresti.getName() + " Typography: " + Carturaresti.getProducts());


        var ArtOfWar = new Book("Random Manufacturer", 56788, (float) 20, (float) (11.5), 20);
        var PeaceandWar = new Book("Random Manufacturer 2", 45647, (float) 16, (float) (9.50), 15, true);
        ArtOfWar.sell(10);
        PeaceandWar.sell(25);
        PeaceandWar.sell(25);


        var l02454 = new Store();
        System.out.println("Number of pharmacies: " + Store.NumberOfPharmacies);
        l02454.addEmployee(65744);
        l02454.addEmployee(73484);
        l02454.printEmployeesList();

        var Order1 = new Order();
        Order1.addProducts(67556, (float) 45.5, (float) 26, 3);
        Order1.addProducts(90429, (float) 10.5, (float) 2.5, 10);
        Order1.orderStats();
        Order.printStats();

        var Return1 = new Return();
        Return1.returnProducts(67556, (float) 45.5, (float) 26, 3);
        Return1.returnProducts(90429, (float) 10.5, (float) 2.5, 10);
        Return1.orderStats();
        Return.printStats();

        var SupplyCar1 = new Delivery();
        SupplyCar1.deliverBook(75438, 45613, 10);
        Delivery.printStats();

    }
}
