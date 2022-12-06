package view;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JLabel;

public class StatsView {
    private static final int FRAME_WIDTH = 400, FRAME_HEIGHT = 500;

    private JButton button1 = new JButton("Close");

    private JLabel label1 = new JLabel("Runtime: 10 minutes");
    private JLabel label2 = new JLabel("No of libraries: 1");
    private JLabel label3 = new JLabel("No of books: 1");
    private JLabel label4 = new JLabel("Robber Probability: 1%");
    private JLabel label5 = new JLabel("Robber Probability: 1%");
    private JLabel label6 = new JLabel("Robber Probability: 1%");

    private JFrame frame = new JFrame();
    private JPanel panel = new JPanel();

    public StatsView() {

        frame.setSize(FRAME_WIDTH, FRAME_HEIGHT);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        panel.setLayout(null);
        frame.add(panel);
        frame.setTitle("Stats Page");

        panel.add(label1);
        label1.setBounds(50, 0, 600, 50);
        panel.add(label2);
        label2.setBounds(50, 50, 600, 50);
        panel.add(label3);
        label3.setBounds(50, 100, 600, 50);
        panel.add(label4);
        label4.setBounds(50, 150, 600, 50);
        panel.add(label5);
        label5.setBounds(50, 200, 600, 50);
        panel.add(label6);
        label6.setBounds(50, 250, 600, 50);

        panel.add(button1);
        button1.setBounds(50, 350, 200, 30);

        button1.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                frame.dispose();
            }
        });
    }

    public void updateStats(int runtime,
            int customerCount,
            double totalSales,
            double totalProfit,
            double totalRobbedMoney,
            double averageChekout) {
        label1.setText("Runtime in virtual minutes: " + runtime);
        label2.setText("Total number of customers: " + customerCount);
        label3.setText("Total sales: " + totalSales + " lei");
        label4.setText("Total profit: " + totalProfit + " lei");
        label5.setText("Total money robbed from libraries: " + totalRobbedMoney + " lei");
        label6.setText("Average checkout: " + averageChekout + " lei");
    }

}
