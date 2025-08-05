package com.example.personal.expense.tracker;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class Category {
    private int id;
    private String name;

    public Category(int id, String name) {
        this.id = id;
        this.name = name;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public static List<Category> getCategories() {
        List<Category> categories = new ArrayList<>();
        try (Connection conn = DriverManager.getConnection("jdbc:sqlite:expenses.db")) {
            PreparedStatement stmt = conn.prepareStatement("SELECT * FROM categories");
            ResultSet rs = stmt.executeQuery();
            while (rs.next()) {
                Category category = new Category(
                        rs.getInt("id"),
                        rs.getString("name"));
                categories.add(category);
            }
        } catch (SQLException e) {
            System.err.println(e.getMessage());
        }
        return categories;
    }

    public static void addCategory(String name) {
        try (Connection conn = DriverManager.getConnection("jdbc:sqlite:expenses.db")) {
            PreparedStatement stmt = conn.prepareStatement("INSERT INTO categories (name) VALUES (?)");
            stmt.setString(1, name);
            stmt.executeUpdate();
        } catch (SQLException e) {
            System.err.println(e.getMessage());
        }
    }

    public static void editCategory(int id, String name) {
        try (Connection conn = DriverManager.getConnection("jdbc:sqlite:expenses.db")) {
            PreparedStatement stmt = conn.prepareStatement("UPDATE categories SET name = ? WHERE id = ?");
            stmt.setString(1, name);
            stmt.setInt(2, id);
            stmt.executeUpdate();
        } catch (SQLException e) {
            System.err.println(e.getMessage());
        }
    }

    public static void deleteCategory(int id) {
        try (Connection conn = DriverManager.getConnection("jdbc:sqlite:expenses.db")) {
            PreparedStatement stmt = conn.prepareStatement("DELETE FROM categories WHERE id = ?");
            stmt.setInt(1, id);
            stmt.executeUpdate();
        } catch (SQLException e) {
            System.err.println(e.getMessage());
        }
    }

    public Category(String name) {
        this(0, name);
    }
}
