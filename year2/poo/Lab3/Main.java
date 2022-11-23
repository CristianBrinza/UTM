package Lab3;

import Lab2.src.Storage;
import Lab2.src.Store;
import Lab2.src.Delivery;
import Lab2.src.Storage;
import Lab3.src.*;



public class Main {
    public static void main(String[] args) {
        var Customer1 = new Customer("Ion", 54436);
        Customer1.createOrder(87960, 5);
        System.out.println("Number of customers: " + Customer.customerCount);

        var Librarian1 = new Librarian("Vasile");
        Librarian1.prescribeDrug(92490, 78942);

        var Carturaresti = new Tyography("Carturaresti");
        Carturaresti.addProduct(56787);
        Carturaresti.addProduct(67879);
        System.out.println("The list of all products of the " + Carturaresti.getName() + " company: " + Carturaresti.getProducts());

        Storage.addStats((float) 20000, (float) 5300, 20);
        Storage.addStats((float) 2050, (float) 570, 5);
        Storage.printReport();

        var Order1 = new Order();
        Order1.addProducts(67556, (float) 45.5, (float) 26, 3);
        Order1.addProducts(90429, (float) 10.5, (float) 2.5, 10);
        Order1.orderStats();
        Order.printStats();

        var Casier1 = new Casier("Vasila",76855);
        Casier1.sellbookss(76859, 87905, 80, true);

        var l0435 = new Store();
        System.out.println("Number of pharmacies: " + Store.NumberOfPharmacies);
        l0435.addEmployee(65744);
        l0435.addEmployee(73484);
        l0435.printEmployeesList();

        var ArtOfWar = new Book("Random Manufacturer", 56788, (float) 20, (float) (11.5), 20);
        var WarAndPeace = new Book("Random Manufacturer 2", 45647, (float) 16, (float) (9.50), 15, true);
        ArtOfWar.sell(10);
        WarAndPeace.sell(25);
        WarAndPeace.sell(25);

        var Return1 = new Return();
        Return1.returnProducts(67556, (float) 45.5, (float) 26, 3);
        Return1.returnProducts(90429, (float) 10.5, (float) 2.5, 10);
        Return1.orderStats();
        Return.printStats();

        var SecurityCar1 = new Security();
        SecurityCar1.arrestRobber(78943);
        SecurityCar1.arrestRobber(54637);

        var SupplyCar1 = new Delivery();
        SupplyCar1.deliverProduct(75438, 45613, 10);
        Delivery.printStats();

    }
}