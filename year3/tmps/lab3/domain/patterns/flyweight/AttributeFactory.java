package domain.patterns.flyweight;

import domain.models.Author;
import domain.models.Genre;

import java.util.HashMap;
import java.util.Map;

// Factory to produce shared attributes (like genre or author) and store them for reuse
public class AttributeFactory {
    private Map<String, Author> authorMap;

    public AttributeFactory() {
        authorMap = new HashMap<>();
    }

    // Get genre from the factory. If it doesn't exist, return the corresponding enum value.
    public Genre getGenre(String genreName) {
        try {
            return Genre.valueOf(genreName.toUpperCase());
        } catch (IllegalArgumentException e) {
            return null;  // Or handle the exception as needed
        }
    }

    // Get author from the factory. If it doesn't exist, create a new one.
    public Author getAuthor(String authorName) {
        Author author = authorMap.get(authorName);
        if (author == null) {
            author = new Author(authorName, "Unknown");  // Using a placeholder for the country
            authorMap.put(authorName, author);
        }
        return author;
    }
}
