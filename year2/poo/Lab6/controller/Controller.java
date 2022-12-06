package controller;

import model.*;
import view.ConfigurationMenuView;
import view.StatsView;

import java.util.Random;

public class Controller {
    private ConfigurationMenuView ConfigurationView;
    private StatsView ResultPageView;

    public Controller() {
    }

    public void runConfiguration(ConfigurationMenuView ConfigurationView) {
        this.ConfigurationView = ConfigurationView;
        while (ConfigurationView.getRunning()) {
            System.out.println(" ");
        }
        Config.NumberOfLibraries = this.ConfigurationView.getLibraries();
        Config.Runtime = this.ConfigurationView.getRuntime();
        Config.NumberOfProducts = this.ConfigurationView.getProducts();
        Config.RobberProbability = this.ConfigurationView.getProbability();
    }

    public void runSimulation() {
        Library[] libraries = new Library[Config.NumberOfLibraries];
        Security[] securityCars = new Security[Config.NumberOfSecurityCars];
        Product[] products = new Product[Config.NumberOfProducts];
        SupplementDelivery car = new SupplementDelivery();
        Random rand = new Random();
        Customer.setRobberProbability(Config.RobberProbability);

        for (int i = 0; i < securityCars.length; i++) {
            securityCars[i] = new Security();
        }

        for (int i = 0; i < libraries.length; i++) {
            libraries[i] = new Library();
            libraries[i].setLibrarian(new Librarian());
            libraries[i].setSecurityCar(securityCars[i % securityCars.length]);
            libraries[i].setDeliveryCar(car);
        }

        double price, productionCost;
        boolean needsOrder;
        for (int i = 0; i < products.length; i++) {
            price = rand.nextFloat();
            productionCost = price * rand.nextFloat();
            needsOrder = rand.nextInt(100) > 70;
            products[i] = new Product(price, productionCost, rand.nextInt(),
                    needsOrder);
            for (int j = 0; j < libraries.length; j++) {
                libraries[j].supplyStock(products[i]);
            }
        }

        int minute = 0;
        boolean addsProducts;
        while (minute <= Config.Runtime) {
            for (int i = 0; i < libraries.length; i++) {
                int currentCustomersPerMinute = libraries[i].generateNumberOfCustomers();
                while (currentCustomersPerMinute > 0) {
                    currentCustomersPerMinute -= 1;
                    libraries[i].setCurrentCustomer(new Customer());
                    if (libraries[i].robberInLibrary()) {
                        System.out.println("All the customers ran from the library during the robbery");
                        currentCustomersPerMinute = 0;
                        libraries[i].isRobbed();
                    } else {
                        addsProducts = true;
                        while (addsProducts) {
                            addsProducts = rand.nextInt(100) > 65;
                            libraries[i].addProductToOrder(products[rand.nextInt(products.length)],
                                    rand.nextInt());
                        }
                        libraries[i].finishOrder();
                        try {
                            Thread.sleep(50);
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt();
                        }
                    }
                }
            }
            System.out.println();
            if (minute + 10 < Config.Runtime) {
                System.out.println("======================");
                System.out.println("10 minutes have passed");
                System.out.println("======================");
            }
            if (minute % 60 == 0 && minute > 0) {
                System.out.println(
                        "One hour has passed since the start.\nThe stock for all items will be supplied and \nthe money from the cash register will be taken");
                for (int i = 0; i < products.length; i++) {
                    for (int j = 0; j < libraries.length; j++) {
                        libraries[j].supplyStock(products[i]);
                    }
                }
                for (int i = 0; i < libraries.length; i++) {
                    libraries[i].resetCashRegister();
                }
            }
            minute += 10;
            try {
                Thread.sleep(50);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }

        for (int i = 0; i < libraries.length; i++) {
            libraries[i].resetCashRegister();
        }
    }

    public void runStats(StatsView ResultPageView) {
        this.ResultPageView = ResultPageView;
        this.ResultPageView.updateStats(Config.Runtime, Customer.objectsCount, Library.totalSales,
                Library.totalProfit, Library.totalRobbedMoney, Library.totalSales / Customer.objectsCount);
    }
}
