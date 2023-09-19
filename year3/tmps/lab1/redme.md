# Library Management System

This project is a sample Java project representing a Library Management System. The project is designed following SOLID principles and demonstrates usage of Factory Pattern for object instantiation.

## Structure:
- `client`: Intended for client-side logic (e.g., UI or command-line interaction).
- `domain`: Contains the core logic for the Library Management System.
- `factory`: Contains factories for instantiating main entities like Book, User, and Transaction.
- `models`: Contains the core models/entities used across the system.

## SOLID Principles:
1. **Single Responsibility Principle (SRP)**: Each class is designed with a single responsibility. For instance, the factory classes have the sole responsibility of object instantiation.
2. **Open/Closed Principle**: The system is open for extensions but closed for modifications.
3. **Liskov Substitution Principle**: Derived classes can be substituted for their base classes without affecting the correctness of the program. Currently, our simple system doesn't delve deep into inheritance.
4. **Interface Segregation Principle**: No client should be forced to depend on interfaces they do not use. Currently, our design doesn't use interfaces, but if it did, this principle would be maintained.
5. **Dependency Inversion Principle**: High-level modules should not depend on low-level modules. Both should depend on abstractions. The domain logic (`Library` class) depends on abstractions (models) and not on concrete implementations.
