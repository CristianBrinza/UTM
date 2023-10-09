/**
 * AuthorPrototype Class
 *
 * Description: Abstract class defining the prototype of an author.
 * Design Pattern: Prototype - This pattern involves creating new objects by copying
 *                an existing object, known as the prototype.
 */
public abstract class AuthorPrototype {
    protected final String name;

    // Constructor initializes the author prototype with a name.
    public AuthorPrototype(String name) {
        this.name = name;
    }

    // Method clones the author prototype, to be implemented by concrete subclasses.
    public abstract AuthorPrototype clone();

    // Getter for the author's name.
    public String getName() {
        return name;
    }
}

// Concrete class representing a fiction author, extending the author prototype.
class FictionAuthor extends AuthorPrototype {
    // Constructor initializes the fiction author with a name.
    public FictionAuthor(String name) {
        super(name);
    }

    // Method clones the fiction author.
    @Override
    public AuthorPrototype clone() {
        return new FictionAuthor(this.name);
    }
}
