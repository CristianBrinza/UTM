package factory;

import models.User;

public class UserFactory implements AbstractFactory<User> {
    @Override
    public User create(Object... args) {
        if(args.length < 2) {
            throw new IllegalArgumentException("Not enough arguments to create a user");
        }

        int id = (int) args[0];
        String name = (String) args[1];
        return new User(id, name);
    }
}
