import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class CategoryDAO {
    private Connection connection;

    public CategoryDAO(String databaseLocation) {
        try {
            Class.forName("org.sqlite.JDBC");
            this.connection = DriverManager.getConnection("jdbc:sqlite:" + databaseLocation);
        } catch (ClassNotFoundException | SQLException e) {
            System.out.println("Error connecting to database: " + e.getMessage());
        }
    }

    public List<Category> getCategories() {
        List<Category> categories = new ArrayList<>();
        String query = "SELECT * FROM categories";
        try (Statement statement = this.connection.createStatement(); ResultSet resultSet = statement.executeQuery(query)) {
            while (resultSet.next()) {
                Category category = new Category();
                category.setId(resultSet.getInt("id"));
                category.setName(resultSet.getString("name"));
                categories.add(category);
            }
        } catch (SQLException e) {
            System.out.println("Error retrieving categories: " + e.getMessage());
        }
        return categories;
    }

    public void addCategory(Category category) {
        String query = "INSERT INTO categories (name) VALUES (?)";
        try (PreparedStatement statement = this.connection.prepareStatement(query)) {
            statement.setString(1, category.getName());
            statement.execute();
        } catch (SQLException e) {
            System.out.println("Error adding category: " + e.getMessage());
        }
    }

    public void updateCategory(Category category) {
        String query = "UPDATE categories SET name = ? WHERE id = ?";
        try (PreparedStatement statement = this.connection.prepareStatement(query)) {
            statement.setString(1, category.getName());
            statement.setInt(2, category.getId());
            statement.execute();
        } catch (SQLException e) {
            System.out.println("Error updating category: " + e.getMessage());
        }
    }

    public void deleteCategory(int id) {
        String query = "DELETE FROM categories WHERE id = ?";
        try (PreparedStatement statement = this.connection.prepareStatement(query)) {
            statement.setInt(1, id);
            statement.execute();
        } catch (SQLException e) {
            System.out.println("Error deleting category: " + e.getMessage());
        }
    }
}