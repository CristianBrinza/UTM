
package domain.patterns.flyweight;

import domain.models.Author;
import domain.models.Genre;

import java.util.HashMap;
import java.util.Map;

/**
 * Factory class to produce and manage shared attributes (like genre or author) using the Flyweight pattern.
 * This class ensures that shared attributes like genre and author are not duplicated but are instead 
 * shared among different books to save memory.
 */
public class AttributeFactory {
    private Map<String, Author> authorMap;  // Map to store authors and prevent duplication

    /**
     * Constructor for AttributeFactory. Initializes the author map.
     */
    public AttributeFactory() {
        authorMap = new HashMap<>();
    }

    /**
     * Get genre from the factory. If the genre doesn't exist, it returns the corresponding enum value.
     * 
     * @param genreName Name of the genre.
     * @return Corresponding Genre enum value or null if not found.
     */
    public Genre getGenre(String genreName) {
        try {
            return Genre.valueOf(genreName.toUpperCase());
        } catch (IllegalArgumentException e) {
            return null;  // Or handle the exception as needed
        }
    }

    /**
     * Get author from the factory. If the author doesn't exist in the map, create a new one and store it.
     * 
     * @param authorName Name of the author.
     * @return Author object either retrieved from the map or newly created.
     */
    public Author getAuthor(String authorName) {
        Author author = authorMap.get(authorName);
        if (author == null) {
            author = new Author(authorName, "Unknown");  // Using a placeholder for the country
            authorMap.put(authorName, author);
        }
        return author;
    }
}