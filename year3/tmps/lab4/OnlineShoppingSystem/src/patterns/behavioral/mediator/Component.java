package patterns.behavioral.mediator;


// Colleague interface
public abstract class Component {
    protected ShoppingMediator mediator;

    public Component(ShoppingMediator mediator) {
        this.mediator = mediator;
    }

    public void send(String event) {
        mediator.handle(event, this);
    }

    public abstract void receive(String event);
}

