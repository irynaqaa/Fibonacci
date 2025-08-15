public class ErrorHandling {
    public void handleError(Exception e) {
        // Handle the error
        System.out.println("An error occurred: " + e.getMessage());
    }
    
    private Connection connection;
    
    public ErrorHandling() {
        try {
            connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/transactions", "root", "password");
        } catch (SQLException e) {
            System.out.println("Error connecting to database: " + e.getMessage());
        }
    }
    
    public List<Transaction> getTransactions() {
        List<Transaction> transactions = new ArrayList<>();
        try (Statement statement = connection.createStatement(); ResultSet resultSet = statement.executeQuery("SELECT * FROM transactions")) {
            while (resultSet.next()) {
                Transaction transaction = new Transaction();
                transaction.setId(resultSet.getInt("id"));
                transaction.setCategory(resultSet.getString("category"));
                transaction.setAmount(resultSet.getDouble("amount"));
                transactions.add(transaction);
            }
        } catch (SQLException e) {
            System.out.println("Error retrieving transactions: " + e.getMessage());
        }
        return transactions;
    }
    
    public void exportToCSV(String filePath) {
        try (FileWriter fileWriter = new FileWriter(filePath)) {
            fileWriter.write("Id,Category,Amount
");
            for (Transaction transaction : getTransactions()) {
                fileWriter.write(transaction.getId() + "," + transaction.getCategory() + "," + transaction.getAmount() + "
");
            }
        } catch (IOException e) {
            System.out.println("Error exporting to CSV: " + e.getMessage());
        }
    }
}