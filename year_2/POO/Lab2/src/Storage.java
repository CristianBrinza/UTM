package Lab2.src;

public abstract class Storage {
    public static float Revenue;
    public static float Profit;
    public static int SoldBooks;

    public static void printReport() {
        System.out.println("Total revenue: " + Revenue);
        System.out.println("Total profit: " + Profit);
        System.out.println("Number of sold products: " + SoldBooks);
    }

    public static void addStats(float revenue, float profit, int amount) {
        Revenue += revenue;
        Profit += profit;
        SoldBooks += amount;
    }

}
