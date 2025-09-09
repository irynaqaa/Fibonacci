public class AddTransactionForm {
    private JTextField amountField;
    private JTextField customerIDField;
    private JTextField transactionTypeField;
    private JTextField transactionDateField;

    public AddTransactionForm() {
        // Initialize form fields
        amountField = new JTextField();
        customerIDField = new JTextField();
        transactionTypeField = new JTextField();
        transactionDateField = new JTextField();

        // Add form fields to the layout
        // ...
    }

    public void saveTransaction() {
        // Get form data
        String amount = amountField.getText();
        String customerID = customerIDField.getText();
        String transactionType = transactionTypeField.getText();
        String transactionDate = transactionDateField.getText();

        // Validate form data
        if (amount.isEmpty() || customerID.isEmpty() || transactionType.isEmpty() || transactionDate.isEmpty()) {
            // Handle invalid form data
            // ...
        } else {
            // Save transaction to database
            try {
                // Use parameterized query to prevent SQL injection
                String query = "INSERT INTO transactions (amount, customer_id, transaction_type, transaction_date) VALUES (?, ?, ?, ?)";
                // Execute query
                // ...
            } catch (SQLException e) {
                // Handle database error
                // ...
            }
        }
    }
}