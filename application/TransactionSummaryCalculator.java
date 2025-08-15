public class TransactionSummaryCalculator {
    public double calculateTotalAmount(List<Transaction> transactions) {
        double totalAmount = 0;
        for (Transaction transaction : transactions) {
            totalAmount += transaction.getAmount();
        }
        return totalAmount;
    }
    
    public static void calculateMonthlySummary(int month, int year) {
        // Initialize variables to store total income, total expenses, and balance
        double totalIncome = 0;
        double totalExpenses = 0;
        double balance = 0;
        
        // Retrieve all transactions for the selected month and year
        List<Transaction> transactions = TransactionDAO.getTransactionsForMonth(month, year);
        
        // Iterate through each transaction and update the total income, total expenses, and balance
        for (Transaction transaction : transactions) {
            if (transaction.getType().equals("Income")) {
                totalIncome += transaction.getAmount();
            } else if (transaction.getType().equals("Expense")) {
                totalExpenses += transaction.getAmount();
            }
        }
        
        // Calculate the balance
        balance = totalIncome - totalExpenses;
        
        // Print the monthly summary
        System.out.println("Monthly Summary for " + getMonthName(month) + " " + year);
        System.out.println("Total Income: " + totalIncome);
        System.out.println("Total Expenses: " + totalExpenses);
        System.out.println("Balance: " + balance);
    }
    
    // Helper method to get the month name from the month number
    private static String getMonthName(int month) {
        String[] monthNames = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};
        return monthNames[month - 1];
    }
}