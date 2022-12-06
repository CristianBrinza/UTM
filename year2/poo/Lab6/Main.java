import view.ConfigurationMenuView;
import view.StatsView;
import controller.*;

public class Main {
    public static void main(String[] args) {
        Controller controller = new Controller();

        controller.runConfiguration(new ConfigurationMenuView());
        controller.runSimulation();
        controller.runStats(new StatsView());
    }
}