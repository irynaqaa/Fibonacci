package com.example.personal.expense.tracker;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class Transaction {
    private int id;
    private double amount;
    private String category;
    private LocalDate date;
    private String description;
    private String type;

    public Transaction(int id, double amount, String category, LocalDate date, String description, String type) {
        this.id = id;
        this.amount = amount;
        this.category = category;
        this.date = date;
        this.description = description;
        this.type = type;
    }

    public int getId() {
        return id;
    }

    public double getAmount() {
        return amount;
    }

    public String getCategory() {
        return category;
    }

    public LocalDate getDate() {
        return date;
    }

    public String getDescription() {
        return description;
    }

    public String getType() {
        return type;
    }

    public static List<Transaction> getTransactions() {
        List<Transaction> transactions = new ArrayList<>();
        try (Connection conn = DriverManager.getConnection("jdbc:sqlite:expenses.db")) {
            PreparedStatement stmt = conn.prepareStatement("SELECT * FROM transactions");
            ResultSet rs = stmt.executeQuery();
            while (rs.next()) {
                Transaction transaction = new Transaction(
                        rs.getInt("id"),
                        rs.getDouble("amount"),
                        rs.getString("category"),
                        rs.getDate("date").toLocalDate(),
                        rs.getString("description"),
                        rs.getString("type"));
                transactions.add(transaction);
            }
        } catch (SQLException e) {
            System.err.println(e.getMessage());
        }
        return transactions;
    }

    public static void addTransaction(double amount, String category, LocalDate date, String description, String type) {
        try (Connection conn = DriverManager.getConnection("jdbc:sqlite:expenses.db")) {
            PreparedStatement stmt = conn.prepareStatement("INSERT INTO transactions (amount, category, date, description, type) VALUES (?, ?, ?, ?, ?)");
            stmt.setDouble(1, amount);
            stmt.setString(2, category);
            stmt.setDate(3, java.sql.Date.valueOf(date));
            stmt.setString(4, description);
            stmt.setString(5, type);
            stmt.executeUpdate();
        } catch (SQLException e) {
            System.err.println(e.getMessage());
        }
    }

    public static void editTransaction(int id, double amount, String category, LocalDate date, String description, String type) {
        try (Connection conn = DriverManager.getConnection("jdbc:sqlite:expenses.db")) {
            PreparedStatement stmt = conn.prepareStatement("UPDATE transactions SET amount = ?, category = ?, date = ?, description = ?, type = ? WHERE id = ?");
            stmt.setDouble(1, amount);
            stmt.setString(2, category);
            stmt.setDate(3, java.sql.Date.valueOf(date));
            stmt.setString(4, description);
            stmt.setString(5, type);
            stmt.setInt(6, id);
            stmt.executeUpdate();
        } catch (SQLException e) {
            System.err.println(e.getMessage());
        }
    }

    public static void deleteTransaction(int id) {
        try (Connection conn = DriverManager.getConnection("jdbc:sqlite:expenses.db")) {
            PreparedStatement stmt = conn.prepareStatement("DELETE FROM transactions WHERE id = ?");
            stmt.setInt(1, id);
            stmt.executeUpdate();
        } catch (SQLException e) {
            System.err.println(e.getMessage());
        }
    }

    public Transaction(double amount, String category, String date, String description, String type) {
        this(0, amount, category, LocalDate.parse(date), description, type);
    }
}
