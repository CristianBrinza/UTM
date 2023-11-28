package patterns.behavioral.chainOfResponsibility;


import domain.Order;

// Handler interface declaring a method for processing an order
public interface OrderHandler {
    void setNextHandler(OrderHandler nextHandler);
    void process(Order order);
}

