/application/src/main/java/com/personal/expense/tracker/Main.java
package com.personal.expense.tracker;

import javafx.application.Application;
import javafx.stage.Stage;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Logger;
import java.util.Scanner;
import java.util.logging.Level;

/**
 * The main class for the Personal Expense Tracker application.
 */
public class Main extends Application {
    private static final Logger LOGGER = Logger.getLogger(Main.class.getName());
    private static final String DB_URL = "jdbc:sqlite:expense_tracker.db";
    private static Connection conn;

    @Override
    public void start(final Stage primaryStage) {
        try {
            // Create a new database if it doesn't exist
            conn = DriverManager.getConnection(DB_URL);
            createTables();
        } catch (SQLException ex) {
            LOGGER.log(Level.SEVERE, null, ex);
        }
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("1. Add transaction");
            System.out.println("2. View transactions");
            System.out.println("3. Exit");
            System.out.print("Choose an option: ");
            int option = scanner.nextInt();
            switch (option) {
                case 1:
                    addTransaction(scanner);
                    break;
                case 2:
                    viewTransactions();
                    break;
                case 3:
                    System.exit(0);
                default:
                    System.out.println("Invalid option");
            }
        }
    }

    private static void createTables() throws SQLException {
        String transactionTable = "CREATE TABLE IF NOT EXISTS transactions (
" +
                "id INTEGER PRIMARY KEY AUTOINCREMENT,
" +
                "date TEXT NOT NULL,
" +
                "category TEXT NOT NULL,
" +
                "type TEXT NOT NULL,
" +
                "amount REAL NOT NULL,
" +
                "description TEXT
" +
                ")";
        String categoryTable = "CREATE TABLE IF NOT EXISTS categories (
" +
                "id INTEGER PRIMARY KEY AUTOINCREMENT,
" +
                "name TEXT NOT NULL,
" +
                "description TEXT
" +
                ")";
        PreparedStatement pstmt = conn.prepareStatement(transactionTable);
        pstmt.execute();
        pstmt = conn.prepareStatement(categoryTable);
        pstmt.execute();
    }

    private static void addTransaction(Scanner scanner) {
        System.out.print("Enter date (yyyy-MM-dd): ");
        String date = scanner.next();
        System.out.print("Enter category: ");
        String category = scanner.next();
        System.out.print("Enter type (income/expense): ");
        String type = scanner.next();
        System.out.print("Enter amount: ");
        double amount = scanner.nextDouble();
        System.out.print("Enter description: ");
        String description = scanner.next();
        Transaction transaction = new Transaction(0, date, category, type, amount, description);
        try {
            PreparedStatement pstmt = conn.prepareStatement("INSERT INTO transactions (date, category, type, amount, description) VALUES (?, ?, ?, ?, ?)");
            pstmt.setString(1, transaction.getDate());
            pstmt.setString(2, transaction.getCategory());
            pstmt.setString(3, transaction.getType());
            pstmt.setDouble(4, transaction.getAmount());
            pstmt.setString(5, transaction.getDescription());
            pstmt.executeUpdate();
            System.out.println("Transaction added successfully");
        } catch (SQLException ex) {
            LOGGER.log(Level.SEVERE, null, ex);
        }
    }

    private static void viewTransactions() {
        try {
            PreparedStatement pstmt = conn.prepareStatement("SELECT * FROM transactions");
            ResultSet rs = pstmt.executeQuery();
            while (rs.next()) {
                Transaction transaction = new Transaction(
                        rs.getInt("id"),
                        rs.getString("date"),
                        rs.getString("category"),
                        rs.getString("type"),
                        rs.getDouble("amount"),
                        rs.getString("description"));
                System.out.println(transaction);
            }
        } catch (SQLException ex) {
            LOGGER.log(Level.SEVERE, null, ex);
        }
    }

    public static void main(final String[] args) {
        launch(args);
    }
}
