package com.personal.expense.tracker;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class ExpenseTracker {
    private Connection connection;

    public ExpenseTracker() {
        try {
            connection = DriverManager.getConnection("jdbc:sqlite:expenses.db");
        } catch (SQLException e) {
            System.out.println("Error connecting to database: " + e.getMessage());
        }
    }

    public void addTransaction(Transaction transaction) {
        try (PreparedStatement statement = connection.prepareStatement("INSERT INTO transactions (date, category, type, amount, description) VALUES (?, ?, ?, ?, ?)")) {
            statement.setString(1, transaction.getDate());
            statement.setString(2, transaction.getCategory());
            statement.setString(3, transaction.getType());
            statement.setDouble(4, transaction.getAmount());
            statement.setString(5, transaction.getDescription());
            statement.executeUpdate();
        } catch (SQLException e) {
            System.out.println("Error adding transaction: " + e.getMessage());
        }
    }

    public List<Transaction> getTransactions() {
        List<Transaction> transactions = new ArrayList<>();
        try (PreparedStatement statement = connection.prepareStatement("SELECT * FROM transactions"); ResultSet resultSet = statement.executeQuery()) {
            while (resultSet.next()) {
                Transaction transaction = new Transaction(
                        resultSet.getInt("id"),
                        resultSet.getString("date"),
                        resultSet.getString("category"),
                        resultSet.getString("type"),
                        resultSet.getDouble("amount"),
                        resultSet.getString("description")
                );
                transactions.add(transaction);
            }
        } catch (SQLException e) {
            System.out.println("Error retrieving transactions: " + e.getMessage());
        }
        return transactions;
    }

    public void close() {
        try {
            connection.close();
        } catch (SQLException e) {
            System.out.println("Error closing database connection: " + e.getMessage());
        }
    }
}
