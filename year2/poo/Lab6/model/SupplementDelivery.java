package model;

// One delivery car can be assigned to more libraries
public final class SupplementDelivery extends Root implements IDIdentifiable {

    public SupplementDelivery() {
        objectsCount += 1;
        this.id = generateId();
    }


    @Override
    public int getId() {
        return this.id;
    }

}
