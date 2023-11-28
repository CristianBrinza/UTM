package patterns.creational.builder;

// Product Class: Represents a complex object being constructed.
public class Computer {
    private String processor;
    private String ram;
    private String storage;

    public void setProcessor(String processor) {
        this.processor = processor;
    }

    public void setRAM(String ram) {
        this.ram = ram;
    }

    public void setStorage(String storage) {
        this.storage = storage;
    }

    public void showSpecs() {
        System.out.println("Computer with Processor: " + processor + ", RAM: " + ram + ", Storage: " + storage);
    }
}

