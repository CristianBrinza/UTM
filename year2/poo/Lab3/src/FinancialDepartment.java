package Lab3.src;

public abstract class FinancialDepartment {
    public static float Revenue;
    public static float Profit;
    public static int SoldProducts;

    public static void printReport() {
        System.out.println("Total revenue: " + Revenue);
        System.out.println("Total profit: " + Profit);
        System.out.println("Number of sold products: " + SoldProducts);
    }

    public static void addStats(float revenue, float profit, int amount) {
        Revenue += revenue;
        Profit += profit;
        SoldProducts += amount;
    }

}
