package com.example.personal.expense.tracker;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class ReportGenerator {
    public static List<Transaction> getTransactionsByDate(LocalDate date) {
        List<Transaction> transactions = new ArrayList<>();
        try (Connection conn = DriverManager.getConnection("jdbc:sqlite:expenses.db")) {
            PreparedStatement stmt = conn.prepareStatement("SELECT * FROM transactions WHERE date = ?");
            stmt.setDate(1, java.sql.Date.valueOf(date));
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

    public static List<Transaction> getTransactionsByCategory(String category) {
        List<Transaction> transactions = new ArrayList<>();
        try (Connection conn = DriverManager.getConnection("jdbc:sqlite:expenses.db")) {
            PreparedStatement stmt = conn.prepareStatement("SELECT * FROM transactions WHERE category = ?");
            stmt.setString(1, category);
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

    public static List<Transaction> getTransactionsByType(String type) {
        List<Transaction> transactions = new ArrayList<>();
        try (Connection conn = DriverManager.getConnection("jdbc:sqlite:expenses.db")) {
            PreparedStatement stmt = conn.prepareStatement("SELECT * FROM transactions WHERE type = ?");
            stmt.setString(1, type);
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
}
