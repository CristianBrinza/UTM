package Lab2.src;

import java.util.Arrays;

public class Member {
    public static int memberCount;

    private int id;
    private String name;

    private String booksarr[];

    public Member(String name) {
        memberCount += 1;
        this.id = generateMemberId();
        this.name = name;

    }

    public void buyBook(int productId, int amount) {
        System.out.println(
                "Member with id " + this.id + " ordered " + amount + " product/products with id " + productId);
    }
    public void showOrders() {
        System.out.println(
                "Customer with id " + this.id + " name " +  this.name );
        System.out.print("Books" );
        System.out.println(Arrays.toString(booksarr));
    }
    private int generateMemberId() {
        return (int) ((Math.random() * (99999 - 10000)) + 10000);
    }

    public int getId() {
        return this.id;
    }

    public String getName() {
        return this.name;
    }
}
