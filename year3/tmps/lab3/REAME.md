### Structure:

-  lab3 - Root directory
    - client - Contains the client code (Main.java)
    - domain - Contains domain logic, further divided into:
        - models - Contains domain models 
            - Author
            - Book
            - Genre
            - Order
        - patterns - Contains implementations of various design patterns:
            - adapter - Adapter pattern implementation (ThirdPartyPrinter, PrinterAdapter)
            - bridge - Bridge pattern implementation (PrintTechnique, DigitalPrint, ScreenPrint, Lithography)
            - builder - Builder pattern implementation (BookBuilder)
            - composite - Composite pattern implementation (BookComponent, SingleBook, BookCollection)
            - decorator - Decorator pattern implementation (BookDecorator, BonusContentDecorator, SignatureDecorator, HardcoverDecorator)
            - facade - Facade pattern implementation (BookProductionFacade)
            - flyweight - Flyweight pattern implementation (AttributeFactory)
            - proxy - Proxy pattern implementation (DigitalBook, RealDigitalBook, DigitalBookProxy)


### Main.java client code:

- Builder Pattern: A BookBuilder is used to build a sample book.
- Bridge Pattern: The sampleBook is printed, and then a new DigitalPrint technique is applied to it.
- Composite Pattern: Two books are created, and both are added to a BookCollection. The collection details are then printed.
- Decorator Pattern: The first book (book1) is decorated with a SignatureDecorator and a  HardcoverDecorator, after which its details are printed.
- Facade Pattern: The BookProductionFacade is used to produce books and add them to inventory.
- Flyweight Pattern: A Book is created using the AttributeFactory to demonstrate the Flyweight pattern.
- Proxy Pattern: A digital book (RealDigitalBook) is created. Two proxies for the digital book are also created, one with a license and one without. Both proxies are then read.