import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

public class Main {
    private Connection connection;
    private TransactionDAO transactionDAO;
    private TransactionFilter filter;

    public Main() {
        try {
            connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/transactions", "root", "password");
            transactionDAO = new TransactionDAO();
            filter = new TransactionFilter();
        } catch (SQLException e) {
            System.out.println("Error connecting to database: " + e.getMessage());
        }
    }

    public void run() {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("1. Export transactions to CSV");
            System.out.println("2. Filter transactions");
            System.out.println("3. Exit");
            System.out.print("Choose an option: ");
            int option = scanner.nextInt();
            switch (option) {
                case 1:
                    System.out.print("Enter file path: ");
                    String filePath = scanner.next();
                    transactionDAO.exportToCSV(filePath);
                    break;
                case 2:
                    System.out.print("Enter date (yyyy-MM-dd): ");
                    String date = scanner.next();
                    List<Transaction> transactions = transactionDAO.getTransactions();
                    List<Transaction> filteredTransactions = filter.filterTransactionsByDate(transactions, date);
                    for (Transaction transaction : filteredTransactions) {
                        System.out.println(transaction);
                    }
                    break;
                case 3:
                    System.exit(0);
                default:
                    System.out.println("Invalid option");
            }
        }
    }

    public static void main(String[] args) {
        Main main = new Main();
        main.run();
    }
}