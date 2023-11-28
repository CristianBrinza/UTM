package patterns.creational.singleton;

// Singleton Class: Manages user sessions across the application.
public class SessionManager {
    private static SessionManager instance;
    private String currentUser;

    private SessionManager() {}

    public static synchronized SessionManager getInstance() {
        if (instance == null) {
            instance = new SessionManager();
        }
        return instance;
    }

    public void setCurrentUser(String user) {
        currentUser = user;
    }

    public String getCurrentUser() {
        return currentUser;
    }

    // Additional session management methods
    public void logOut() {
        currentUser = null;
    }
}

