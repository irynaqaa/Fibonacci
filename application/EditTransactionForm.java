public class EditTransactionForm {
    public void editTransaction() {
        // Get user input for transaction details
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter transaction id: ");
        int id = scanner.nextInt();
        System.out.print("Enter new transaction date (yyyy-MM-dd): ");
        String date = scanner.next();
        System.out.print("Enter new transaction category: ");
        String category = scanner.next();
        System.out.print("Enter new transaction amount: ");
        double amount = scanner.nextDouble();
        System.out.print("Enter new transaction type (Income/Expense): ");
        String type = scanner.next();
        
        // Create a new transaction object
        Transaction transaction = new Transaction();
        transaction.setId(id);
        transaction.setDate(date);
        transaction.setCategory(category);
        transaction.setAmount(amount);
        transaction.setType(type);
        
        // Update the transaction in the database
        try {
            Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/transactions", "root", "password");
            PreparedStatement statement = connection.prepareStatement("UPDATE transactions SET date = ?, category = ?, amount = ?, type = ? WHERE id = ?");
            statement.setString(1, date);
            statement.setString(2, category);
            statement.setDouble(3, amount);
            statement.setString(4, type);
            statement.setInt(5, id);
            statement.executeUpdate();
            System.out.println("Transaction updated successfully");
        } catch (SQLException e) {
            System.out.println("Error updating transaction: " + e.getMessage());
        }
    }
}