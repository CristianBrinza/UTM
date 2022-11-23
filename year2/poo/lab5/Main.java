import java.util.Random;

public class Main {
    public static void main ( String[] args ) {

        Library[] libraries = new Library[Config.NumberOfLibraries];
        Security[] securityCars = new Security[Config.NumberOfSecurityCars];
        Book[] products = new Book[Config.NumberOfBooks];
        Delivery car = new Delivery ( );
        Random rand = new Random ( );
        Customer.setRobberProbability (Config.RobberProbability);

        for (int i = 0; i < securityCars.length; i++) {
            securityCars[i] = new Security ( );
        }

        for (int i = 0; i < libraries.length; i++) {
            libraries[i] = new Library ( );
            libraries[i].setLibrarian (new Chasher ( ));
            libraries[i].setSecurityCar (securityCars[i % securityCars.length]);
            libraries[i].setDeliveryCar (car);
        }

        double price, productionCost;
        boolean needsPrescribtion;
        for (int i = 0; i < products.length; i++) {
            price = (float) (Math.random ( ) * 450);
            productionCost = price * (float) (Math.random ( ));
            needsPrescribtion = (int) (Math.random ( ) * 100) > 70;
            products[i] = new Book (price , productionCost , (int) (Math.random ( ) * 60 + 20) , needsPrescribtion);
            for (int j = 0; j < libraries.length; j++) {
                libraries[j].supplyStock (products[i]);
            }
        }

        int minute = 0;
        boolean addsBooks;
        while (minute <= Config.Runtime) {
            for (int i = 0; i < libraries.length; i++) {
                int currentCustomersPerMinute = libraries[i].generateNumberOfCustomers ( );
                while (currentCustomersPerMinute > 0) {
                    currentCustomersPerMinute -= 1;
                    libraries[i].setCurrentCustomer (new Customer ( ));
                    if (libraries[i].robberInLibrary ( )) {
                        currentCustomersPerMinute = 0;
                        System.out.println ("All the customers ran from the library during the robbery");
                        libraries[i].isRobbed ( );
                    } else {
                        addsBooks = true;
                        while (addsBooks) {
                            addsBooks = (int) (Math.random ( ) * 100) > 65;
                            libraries[i].addBookToOrder (products[rand.nextInt (products.length)] , (int) (Math.random ( ) * (25 - 1) + 1));

                        }
                        libraries[i].finishOrder ( );
                        try {
                            Thread.sleep (2500);
                        } catch (InterruptedException e) {
                            Thread.currentThread ( ).interrupt ( );
                        }
                    }
                }
            }
            System.out.println ( );
            if (minute + 10 < Config.Runtime) {
                System.out.println ("==========================================");
                System.out.println ("           10 minutes have passed");
                System.out.println ("==========================================");
            }
            if (minute % Config.CashRegisterRefreshCooldown == 0 && minute > 0) {
                System.out.println ("________________________________________________________");
                System.out.println ("*   " + Config.CashRegisterRefreshCooldown + " minutes have passed since the last cash register refresh.\nNow the money from all the cash registers will be taken");

                for (int i = 0; i < libraries.length; i++) {
                    libraries[i].resetCashRegister ( );
                }
            }
            if (minute % Config.StockSupplyCooldown == 0 && minute > 0) {
                System.out.println ("________________________________________________________");
                System.out.println (Config.StockSupplyCooldown + " minutes have passed since last delivery\nThe stock for all items will be supplied");
                for (int i = 0; i < products.length; i++) {
                    for (int j = 0; j < libraries.length; j++) {
                        libraries[j].supplyStock (products[i]);
                    }
                }
            }
            minute += 10;
            try {
                Thread.sleep (3000);
            } catch (InterruptedException e) {
                Thread.currentThread ( ).interrupt ( );
            }
        }

        for (int i = 0; i < libraries.length; i++) {
            libraries[i].resetCashRegister ( );
        }

        System.out.println ("+=================================================+");
        System.out.println ("|               Simulation Results                |");
        System.out.println ("+=================================================+");
        System.out.println ("Time in virtual minutes have passed:    " + (minute - 10));
        System.out.println ("Total number of customers:              " + Customer.objectsCount);
        System.out.println ("Total sales:                            " + Library.totalSales + " lei");
        System.out.println ("Total profit:                           " + Library.totalProfit + " lei");
        System.out.println ("Total money robbed from libraries:      " + Library.totalRobbedMoney + " lei");
        System.out.println ("Average chekout:                        " + Library.totalSales / Customer.objectsCount + " lei");
        System.out.println ("+=================================================+");
    }
}